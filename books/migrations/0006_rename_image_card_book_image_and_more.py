# Generated by Django 4.2 on 2024-01-10 20:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0005_alter_comment_active"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="image_card",
            new_name="image",
        ),
        migrations.RemoveField(
            model_name="book",
            name="image_detail",
        ),
    ]