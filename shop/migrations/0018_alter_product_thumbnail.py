# Generated by Django 3.2 on 2021-10-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_rename_user_productreview_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='photo_path'),
        ),
    ]
