# Generated by Django 3.0.3 on 2020-02-28 09:50

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200228_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path),
        ),
    ]
