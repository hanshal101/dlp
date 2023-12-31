# Generated by Django 4.1.7 on 2023-11-16 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.class')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.teachers')),
            ],
        ),
    ]
