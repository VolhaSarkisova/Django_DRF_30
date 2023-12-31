# Generated by Django 4.0 on 2023-09-02 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Enter a comment', max_length=3000, verbose_name='Comment')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
