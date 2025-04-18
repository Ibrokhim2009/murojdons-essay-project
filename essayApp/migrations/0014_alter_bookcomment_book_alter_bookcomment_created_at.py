# Generated by Django 5.2 on 2025-04-07 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("essayApp", "0013_alter_bookthemes_theme"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookcomment",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="essayApp.book",
            ),
        ),
        migrations.AlterField(
            model_name="bookcomment",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
