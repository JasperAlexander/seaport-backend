# Generated by Django 4.1 on 2022-08-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_orderoffers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="identifierOrCriteria",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="offer",
            name="token",
            field=models.CharField(max_length=200),
        ),
    ]