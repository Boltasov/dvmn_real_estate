from django.db import migrations


def link_owners_to_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    flats = Flat.objects.all()
    for flat in flats:
        owner, _ = Owner.objects.get_or_create(name=flat.owner,
                                               owner_phonenumber=flat.owners_phonenumber,
                                               owner_pure_phone=flat.owner_pure_phone)
        owner.flats.add(flat)


class Migration(migrations.Migration):
    dependencies = [('property', 'create_owners')]

    operations = [
        migrations.RunPython(link_owners_to_flats),
        ]
