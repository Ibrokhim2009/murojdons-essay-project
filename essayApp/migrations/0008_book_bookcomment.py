# Generated by Django 5.2 on 2025-04-07 18:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("essayApp", "0007_questionforessay"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("short_description", models.CharField(max_length=90)),
                (
                    "banner",
                    models.ImageField(blank=True, null=True, upload_to="media/"),
                ),
                ("banner_url", models.URLField(blank=True, null=True)),
                ("theme_title", models.CharField(max_length=90)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("author", models.CharField(verbose_name=130)),
                ("theme_description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="BookComment",
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
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="book_comments",
                        to="essayApp.book",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
