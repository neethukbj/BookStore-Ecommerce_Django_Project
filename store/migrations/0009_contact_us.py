# Generated by Django 4.2 on 2023-06-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_description_alter_product_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
