# Generated by Django 4.2.7 on 2023-12-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="subcategory", name="category",),
        migrations.AddField(
            model_name="subcategory",
            name="categories",
            field=models.ManyToManyField(to="categories.category"),
        ),
    ]
