# Generated by Django 3.2 on 2021-10-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20211021_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_available',
            field=models.IntegerField(default=0),
        ),
    ]