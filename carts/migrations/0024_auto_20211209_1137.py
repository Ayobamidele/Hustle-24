# Generated by Django 3.2 on 2021-12-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0023_rename_is_active_shippingaddresscustomer_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddresscustomer',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='shippingaddressorder',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
    ]
