# Generated by Django 3.2 on 2022-01-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_vendor_is_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='orders',
            field=models.IntegerField(default=0),
        ),
    ]