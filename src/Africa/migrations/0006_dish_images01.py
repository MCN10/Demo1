# Generated by Django 3.0.8 on 2020-07-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Africa', '0005_auto_20200731_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='images01',
            field=models.ImageField(default=1, upload_to='main_product/'),
            preserve_default=False,
        ),
    ]
