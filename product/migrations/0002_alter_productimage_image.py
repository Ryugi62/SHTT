# Generated by Django 5.0 on 2023-12-08 07:54

import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=product.models.generate_unique_filename),
        ),
    ]