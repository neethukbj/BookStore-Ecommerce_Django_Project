# Generated by Django 4.2 on 2023-06-24 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_paid_order_payment_id_order_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additional_info',
        ),
    ]
