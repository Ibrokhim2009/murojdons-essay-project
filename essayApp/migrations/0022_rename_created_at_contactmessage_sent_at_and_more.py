# Generated by Django 5.2 on 2025-04-09 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("essayApp", "0021_contactmessage"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="contactmessage",
            old_name="created_at",
            new_name="sent_at",
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="contactmessage",
            name="name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
