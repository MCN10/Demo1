# Generated by Django 3.0.8 on 2020-08-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_account_is_axisstaff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=200, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30, verbose_name='Full Name'),
        ),
    ]
