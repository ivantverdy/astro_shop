# Generated by Django 5.1.1 on 2024-09-13 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astro_shop', '0002_alter_category_options_product_current_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_available',
            new_name='for_sale',
        ),
    ]