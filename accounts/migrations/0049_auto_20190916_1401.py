# Generated by Django 2.1.7 on 2019-09-16 11:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_auto_20190912_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastudent',
            name='admission_date',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=100),
        ),
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 16, 11, 1, 29, 214770, tzinfo=utc)),
        ),
    ]