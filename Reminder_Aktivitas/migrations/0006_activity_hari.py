# Generated by Django 3.2.7 on 2021-11-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder_Aktivitas', '0005_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='hari',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]