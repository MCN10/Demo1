# Generated by Django 3.0.8 on 2020-07-31 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Africa', '0004_auto_20200731_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='image01',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='image02',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='image03',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='image04',
        ),
    ]
