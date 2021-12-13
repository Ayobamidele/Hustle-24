# Generated by Django 3.2 on 2021-12-06 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_customer_profile_pic'),
        ('carts', '0012_shippingaddresscustomer_shippingaddressorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddresscustomer',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='shippingaddressorder',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='shippingaddressorder',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.order'),
        ),
        migrations.CreateModel(
            name='ShippingPaymentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.BigIntegerField(max_length=16)),
                ('name_on_card', models.CharField(max_length=200)),
                ('expiry_month', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], max_length=2)),
                ('expiry_year', models.CharField(choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035)], max_length=4)),
                ('security_code', models.CharField(max_length=4)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.order')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingPaymentCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.BigIntegerField(max_length=16)),
                ('name_on_card', models.CharField(max_length=200)),
                ('expiry_month', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], max_length=2)),
                ('expiry_year', models.CharField(choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035)], max_length=4)),
                ('security_code', models.CharField(max_length=4)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]