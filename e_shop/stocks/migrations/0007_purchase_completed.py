# Generated by Django 5.0 on 2024-01-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0006_alter_purchase_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
