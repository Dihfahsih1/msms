# Generated by Django 2.1.7 on 2019-08-22 06:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20190821_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='Amount',
            new_name='Percentage',
        ),
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=datetime.datetime(2019, 8, 22, 6, 43, 47, 52668, tzinfo=utc)),
        ),
    ]
