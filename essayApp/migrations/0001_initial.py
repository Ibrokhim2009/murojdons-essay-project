# Generated by Django 5.2 on 2025-04-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Podcast",
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
                ("title", models.CharField(max_length=70)),
                ("description", models.TextField()),
                ("video_url", models.URLField(blank=True, null=True)),
                ("banner", models.ImageField(upload_to="media/")),
            ],
        ),
    ]
