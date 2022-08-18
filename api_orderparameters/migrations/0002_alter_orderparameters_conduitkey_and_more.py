# Generated by Django 4.1 on 2022-08-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_orderparameters", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderparameters",
            name="conduitKey",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="orderparameters",
            name="endTime",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="orderparameters",
            name="offerer",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="orderparameters",
            name="salt",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="orderparameters",
            name="startTime",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="orderparameters",
            name="zone",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="orderparameters",
            name="zoneHash",
            field=models.CharField(max_length=200),
        ),
    ]