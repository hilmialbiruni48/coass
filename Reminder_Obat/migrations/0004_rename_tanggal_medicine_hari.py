# Generated by Django 3.2.7 on 2021-11-05 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder_Obat', '0003_medicine_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='tanggal',
            new_name='hari',
        ),
    ]
