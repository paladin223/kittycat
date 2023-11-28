# Generated by Django 3.2.16 on 2023-11-22 17:11

from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cats", "0005_auto_20231120_0220"),
    ]

    operations = [
        migrations.AddField(
            model_name="cat",
            name="like",
            field=models.ManyToManyField(
                related_name="like", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
