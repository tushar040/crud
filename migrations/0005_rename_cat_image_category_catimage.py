# Generated by Django 4.2.5 on 2023-10-09 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0004_product_product_price_product_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_image',
            new_name='catimage',
        ),
    ]
