# Generated by Django 3.0.3 on 2020-02-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200229_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='productItem', unique=True),
        ),
    ]
