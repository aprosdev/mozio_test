# Generated by Django 3.2.16 on 2022-12-19 00:04

from django.db import migrations, models
import mozio_api.geojsonfield
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phoneNumber', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mozio',
                'ordering': ['-createdAt'],
            },
        ),
        migrations.CreateModel(
            name='ServiceAreaModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.FloatField()),
                ('geoJson', mozio_api.geojsonfield.GeoJSONSchemaField(blank=True, default=dict)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
    ]