# Generated by Django 3.0.8 on 2020-08-07 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collective', '0008_auto_20200806_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectiveproduct',
            name='digital',
        ),
        migrations.RemoveField(
            model_name='collectiveshippingaddress',
            name='address',
        ),
        migrations.RemoveField(
            model_name='collectiveshippingaddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='collectiveshippingaddress',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='collectiveproduct',
            name='stock',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectiveshippingaddress',
            name='address1',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectiveshippingaddress',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='collectiveshippingaddress',
            name='country',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectiveshippingaddress',
            name='postal_code',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectiveshippingaddress',
            name='province',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectiveshippingaddress',
            name='suburb',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='collectiveshippingaddress',
            name='city',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
