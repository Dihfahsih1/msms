# Generated by Django 2.1.7 on 2019-09-12 08:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_auto_20190912_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 12, 8, 34, 34, 687378, tzinfo=utc)),
        ),
    ]