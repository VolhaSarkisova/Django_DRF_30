# Generated by Django 4.0 on 2023-09-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.CharField(choices=[('низкий', 'низкий'), ('средний', 'средний'), ('высокий', 'высокий')], max_length=10),
        ),
    ]