# Generated by Django 4.0.3 on 2022-04-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_alter_product_productimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productimages',
            field=models.ManyToManyField(blank=True, to='shop.productimage'),
        ),
    ]
