# Generated by Django 4.1 on 2022-08-20 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api_items", "0002_alter_item_recipient"),
        ("api_orders", "0003_remove_order_consideration_remove_order_offer_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="consideration",
        ),
        migrations.RemoveField(
            model_name="order",
            name="offer",
        ),
        migrations.AddField(
            model_name="order",
            name="consideration",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="consideration",
                to="api_items.item",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="offer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="offer",
                to="api_items.item",
            ),
        ),
    ]
