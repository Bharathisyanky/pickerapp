# Generated by Django 4.2.7 on 2023-12-05 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_remove_product_subcategory"),
    ]

    operations = [
        migrations.RemoveField(model_name="stockmovement", name="from_location",),
        migrations.RemoveField(model_name="stockmovement", name="product",),
        migrations.RemoveField(model_name="stockmovement", name="to_location",),
        migrations.DeleteModel(name="LocationCode",),
        migrations.DeleteModel(name="StockMovement",),
    ]
