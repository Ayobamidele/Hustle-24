# Generated by Django 3.2 on 2021-10-22 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20211021_1101'),
        ('accounts', '0005_vendor_storename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='storename',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shop.shop'),
        ),
    ]
