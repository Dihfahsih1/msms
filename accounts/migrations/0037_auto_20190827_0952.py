# Generated by Django 2.1.7 on 2019-08-27 06:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20190827_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastudent',
            name='Guardian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Guardian'),
        ),
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=datetime.datetime(2019, 8, 27, 6, 52, 25, 5646, tzinfo=utc)),
        ),
    ]
