# Generated by Django 3.0.8 on 2020-08-06 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Collective', '0007_collectivecustomer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectiveproduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='collectiveproduct',
            name='size',
        ),
    ]
