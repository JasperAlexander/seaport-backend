# Generated by Django 4.1 on 2022-08-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("symbol", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=50)),
                ("image_url", models.URLField(blank=True)),
                ("name", models.CharField(blank=True, max_length=50)),
                ("decimals", models.IntegerField()),
                ("eth_price", models.IntegerField(blank=True)),
                ("usd_price", models.FloatField(blank=True)),
            ],
        ),
    ]
