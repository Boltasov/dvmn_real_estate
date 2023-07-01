import phonenumbers

from django.db import migrations


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_number):
            flat.owner_pure_phone = phonenumbers.format_number(parsed_number,
                                                               phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            flat.save()


class Migration(migrations.Migration):
    dependencies = [('property', '0003_flat_owner_pure_phone_alter_flat_has_balcony')]

    operations = [
        migrations.RunPython(fill_owner_pure_phone),
        ]
