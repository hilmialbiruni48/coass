# Generated by Django 3.2.7 on 2021-11-04 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Catatan_Kesehatan', '0002_alter_healthrecord_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthrecord',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
