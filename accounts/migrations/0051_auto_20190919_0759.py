# Generated by Django 2.1.7 on 2019-09-19 04:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_auto_20190916_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
