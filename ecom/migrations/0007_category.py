# Generated by Django 3.0.5 on 2024-11-03 16:47

from django.db import migrations, models

def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('ecom', 'Category')
    Category.objects.bulk_create([
        Category(name="Men", description="Men's clothing and accessories"),
        Category(name="Women", description="Women's clothing and accessories"),
        Category(name="Kids", description="Kids' clothing and accessories"),
        Category(name="Accessories", description="Various accessories")
       
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RunPython(create_initial_categories),  # This line will insert the categories
    ]
