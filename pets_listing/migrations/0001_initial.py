# Generated by Django 5.0.4 on 2024-04-11 16:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_file', models.FileField(upload_to='media/')),
                ('type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=250, null=True)),
                ('building', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets_listing.city')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets_listing.region')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets_listing.address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=2000)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets_listing.address')),
                ('breed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pets', to='pets_listing.breed')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets_listing.media')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pets_listing.organization')),
                ('profile_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]