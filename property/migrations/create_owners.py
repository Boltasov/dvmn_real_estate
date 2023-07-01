from django.db import migrations


def create_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    flats = Flat.objects.all()
    for flat in flats.iterator():
        Owner.objects.get_or_create(name=flat.owner,
                                    owner_phonenumber=flat.owners_phonenumber,
                                    owner_pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):
    dependencies = [('property', '0001_alter_flat_likes_owner')]

    operations = [
        migrations.RunPython(create_owners),
        ]
