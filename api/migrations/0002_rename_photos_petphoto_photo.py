# Generated by Django 4.0 on 2021-12-09 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="petphoto",
            old_name="photos",
            new_name="photo",
        ),
    ]
