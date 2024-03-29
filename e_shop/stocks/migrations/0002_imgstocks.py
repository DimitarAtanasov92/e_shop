# Generated by Django 5.0 on 2024-01-20 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImgStocks",
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
                ("img", models.ImageField(upload_to="")),
                (
                    "stocks",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stocks.stock"
                    ),
                ),
            ],
        ),
    ]
