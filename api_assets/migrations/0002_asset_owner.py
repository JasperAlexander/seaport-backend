# Generated by Django 4.1 on 2022-08-07 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api_users", "0002_alter_user_config"),
        ("api_assets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api_users.user",
            ),
        ),
    ]
