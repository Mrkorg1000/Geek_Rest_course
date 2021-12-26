# Generated by Django 4.0 on 2021-12-26 17:30

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("e6357a64-13fb-4428-b646-281bfd6fa0b4"), primary_key=True, serialize=False
            ),
        ),
    ]
