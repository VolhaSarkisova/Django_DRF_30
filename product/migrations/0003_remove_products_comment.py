# Generated by Django 4.0 on 2023-09-02 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_products_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='comment',
        ),
    ]
