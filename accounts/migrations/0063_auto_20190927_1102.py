# Generated by Django 2.1.7 on 2019-09-27 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0062_auto_20190927_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastudent',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='accounts.Sectioninformation'),
        ),
    ]
