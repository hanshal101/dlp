# Generated by Django 4.1.7 on 2023-12-16 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_yearclass'),
        ('student_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='class_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='timetable.yearclass'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdata',
            name='year',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='timetable.year'),
            preserve_default=False,
        ),
    ]
