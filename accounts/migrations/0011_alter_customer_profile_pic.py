# Generated by Django 3.2 on 2021-10-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images.jpg', null=True, upload_to='static/images/'),
        ),
    ]
