# Generated by Django 3.2.7 on 2021-11-04 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder_Aktivitas', '0006_activity_hari'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='hari',
        ),
    ]