# Generated by Django 3.2.7 on 2021-10-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder_Aktivitas', '0002_alter_activity_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='aktivitas',
            field=models.CharField(max_length=30),
        ),
    ]