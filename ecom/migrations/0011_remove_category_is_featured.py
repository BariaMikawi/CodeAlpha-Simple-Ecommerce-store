# Generated by Django 5.1.3 on 2024-11-18 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0010_category_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_featured',
        ),
    ]
