# Generated by Django 4.2.2 on 2023-07-01 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', 'link_owners_to_flats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(db_index=True, verbose_name='Текст жалобы'),
        ),
    ]