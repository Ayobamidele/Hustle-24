# Generated by Django 3.2 on 2021-12-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0020_auto_20211206_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingpaymentcustomer',
            name='card_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shippingpaymentorder',
            name='card_number',
            field=models.IntegerField(),
        ),
    ]
