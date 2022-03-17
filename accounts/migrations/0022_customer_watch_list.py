# Generated by Django 4.0.2 on 2022-03-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watched_products', '0007_watchlist_only_one_price'),
        ('accounts', '0021_watchgroup_watch_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='watch_list',
            field=models.ManyToManyField(related_name='+', to='watched_products.WatchList'),
        ),
    ]
