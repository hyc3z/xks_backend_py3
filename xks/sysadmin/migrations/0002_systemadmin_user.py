# Generated by Django 2.2.11 on 2020-06-14 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sysadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemadmin',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]