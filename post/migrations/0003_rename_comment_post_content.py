# Generated by Django 4.1 on 2023-01-13 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_post_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="comment", new_name="content",
        ),
    ]
