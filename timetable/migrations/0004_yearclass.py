# Generated by Django 4.1.7 on 2023-12-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_year_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='YearClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearclass', models.CharField(max_length=3)),
            ],
        ),
    ]
