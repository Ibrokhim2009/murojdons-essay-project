# Generated by Django 5.2 on 2025-04-08 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("essayApp", "0016_rename_description_forumtopic_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="forumtopic",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
    ]
