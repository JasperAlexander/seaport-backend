# Generated by Django 4.1 on 2022-08-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_events", "0007_alter_event_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="quantity",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="event",
            name="total_price",
            field=models.FloatField(),
        ),
    ]