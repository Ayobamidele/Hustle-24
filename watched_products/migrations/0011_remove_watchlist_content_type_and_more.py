# Generated by Django 4.0.3 on 2022-04-06 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watched_products', '0010_alter_watchlist_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='products',
        ),
    ]
