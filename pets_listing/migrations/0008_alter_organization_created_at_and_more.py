# Generated by Django 5.0.4 on 2024-04-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_listing', '0007_alter_organization_options_alter_pet_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]