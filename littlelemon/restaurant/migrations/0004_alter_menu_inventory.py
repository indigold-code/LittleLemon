# Generated by Django 4.1.7 on 2023-04-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_bookingdate_booking_bookingdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.SmallIntegerField(),
        ),
    ]
