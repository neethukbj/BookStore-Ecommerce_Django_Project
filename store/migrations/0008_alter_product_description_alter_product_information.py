# Generated by Django 4.2 on 2023-06-14 05:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_collections_remove_product_colllection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
