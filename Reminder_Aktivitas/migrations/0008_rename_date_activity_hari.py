# Generated by Django 3.2.7 on 2021-11-04 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder_Aktivitas', '0007_remove_activity_hari'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='date',
            new_name='hari',
        ),
    ]