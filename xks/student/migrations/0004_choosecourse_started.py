# Generated by Django 2.2.11 on 2020-06-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200615_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='choosecourse',
            name='started',
            field=models.BooleanField(default=False),
        ),
    ]