# Generated by Django 3.0.8 on 2020-07-30 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Axis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
