# Generated by Django 3.2.12 on 2022-02-26 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors_appointment_core', '0002_rename_appointmentnotes_appointmentnote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HealthFacilityHours',
            new_name='HealthFacilityHour',
        ),
    ]
