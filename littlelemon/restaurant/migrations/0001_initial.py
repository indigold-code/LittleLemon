# Generated by Django 4.1.7 on 2023-03-30 17:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(99999999999)])),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField(validators=[django.core.validators.MaxValueValidator(6)])),
                ('BookingDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('MenuID', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('Title', models.CharField(max_length=255, unique=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
            ],
        ),
    ]
