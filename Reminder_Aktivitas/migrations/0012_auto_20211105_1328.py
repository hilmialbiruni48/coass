# Generated by Django 3.2.7 on 2021-11-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder_Aktivitas', '0011_auto_20211105_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='waktuakhir',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='waktuawal',
            field=models.TimeField(),
        ),
    ]