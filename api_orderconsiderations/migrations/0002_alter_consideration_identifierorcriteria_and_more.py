# Generated by Django 4.1 on 2022-08-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_orderconsiderations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consideration",
            name="identifierOrCriteria",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="consideration",
            name="recipient",
            field=models.CharField(max_length=2000),
        ),
    ]