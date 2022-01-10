# Generated by Django 3.2 on 2022-01-10 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_remove_product_vendor'),
        ('accounts', '0018_vendor_orders'),
        ('carts', '0034_rename_ordered_cart_delivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.AddField(
            model_name='cart',
            name='vendor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.vendor'),
        ),
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carts.cart')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
