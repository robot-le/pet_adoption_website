# Generated by Django 5.0.4 on 2024-04-17 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_listing', '0008_alter_organization_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pets', to='pets_listing.organization'),
        ),
    ]
