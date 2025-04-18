# Generated by Django 5.2 on 2025-04-08 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("essayApp", "0015_forumtopic_forumcomment"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="forumtopic",
            old_name="description",
            new_name="content",
        ),
        migrations.RemoveField(
            model_name="forumtopic",
            name="updated_at",
        ),
        migrations.AlterField(
            model_name="forumtopic",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
