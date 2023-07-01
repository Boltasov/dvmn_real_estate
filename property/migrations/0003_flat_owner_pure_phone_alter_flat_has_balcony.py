# Generated by Django 4.2.2 on 2023-06-30 04:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_flat_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Наличие балкона'),
        ),
    ]