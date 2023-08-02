# Generated by Django 4.2 on 2023-06-08 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_tag_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='compartments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.compartments'),
            preserve_default=False,
        ),
    ]
