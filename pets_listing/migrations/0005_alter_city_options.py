# Generated by Django 5.0.4 on 2024-04-11 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets_listing', '0004_delete_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
    ]