# Generated by Django 2.1.7 on 2019-09-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_auto_20190920_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=130)),
                ('Notes', models.TextField(max_length=130)),
            ],
        ),
    ]