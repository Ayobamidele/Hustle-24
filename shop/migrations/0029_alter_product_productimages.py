# Generated by Django 4.0.3 on 2022-04-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_rename_shop_name_shop_shopname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productimages',
            field=models.ManyToManyField(blank=True, null=True, to='shop.productimage'),
        ),
    ]
