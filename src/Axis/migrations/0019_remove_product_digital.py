# Generated by Django 3.0.8 on 2020-08-06 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Axis', '0018_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
