# Generated by Django 2.1.7 on 2019-09-26 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_auto_20190926_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='road',
            name='city',
        ),
        migrations.RemoveField(
            model_name='road',
            name='country',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='road',
        ),
    ]
