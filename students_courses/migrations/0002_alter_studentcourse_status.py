# Generated by Django 5.0.1 on 2024-01-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending', max_length=11),
        ),
    ]
