# Generated by Django 4.2 on 2023-06-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_compartments_product_compartments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='compartments',
        ),
        migrations.AddField(
            model_name='product',
            name='compartment',
            field=models.CharField(choices=[('Best Sellers', 'Best Sellers'), ('New Arrivals', 'New Arrivals'), ('Box Sets', 'Box Sets'), ('Todays Deal ', 'Todays Deal')], default=1, max_length=200),
        ),
        migrations.DeleteModel(
            name='Compartments',
        ),
    ]
