# Generated by Django 5.2 on 2025-04-07 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("essayApp", "0009_alter_book_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookThemes",
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
                ("theme", models.CharField(max_length=300)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="theme",
                        to="essayApp.book",
                    ),
                ),
            ],
        ),
    ]
