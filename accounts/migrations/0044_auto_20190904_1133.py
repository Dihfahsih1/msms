# Generated by Django 2.1.7 on 2019-09-04 08:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_auto_20190904_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 4, 8, 33, 51, 915069, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
