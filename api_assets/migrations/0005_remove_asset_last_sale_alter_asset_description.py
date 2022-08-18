# Generated by Django 4.1 on 2022-08-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_assets", "0004_alter_asset_last_sale_alter_asset_orders_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="asset",
            name="last_sale",
        ),
        migrations.AlterField(
            model_name="asset",
            name="description",
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]