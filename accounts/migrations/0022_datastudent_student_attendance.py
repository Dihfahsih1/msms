# Generated by Django 2.1.7 on 2019-08-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_remove_datastudent_student_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastudent',
            name='Student_Attendance',
            field=models.CharField(choices=[('1', 'Present'), ('0', 'Absent')], default='none', max_length=8, null=True),
        ),
    ]
