# Generated by Django 5.2 on 2025-04-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("essayApp", "0012_alter_bookthemes_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookthemes",
            name="theme",
            field=models.TextField(),
        ),
    ]
