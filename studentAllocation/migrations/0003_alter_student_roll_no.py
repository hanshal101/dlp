# Generated by Django 4.1.7 on 2023-12-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentAllocation', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(),
        ),
    ]
