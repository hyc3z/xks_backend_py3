# Generated by Django 3.0.4 on 2020-06-14 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
        ('sysadmin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('sname', models.CharField(max_length=100)),
                ('schoolid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='sysadmin.School')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChooseCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pscore', models.FloatField(default=0)),
                ('kscore', models.FloatField(default=0)),
                ('zscore', models.FloatField(default=0)),
                ('ocid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_score', to='teacher.OfferCourse')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_score', to='student.Student')),
            ],
        ),
    ]