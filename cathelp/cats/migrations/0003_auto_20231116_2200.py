# Generated by Django 3.2.16 on 2023-11-16 19:00

import django.core.validators
from django.db import migrations
from django.db import models

import cats.validator


class Migration(migrations.Migration):
    dependencies = [
        ("cats", "0002_alter_cat_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cat",
            name="age",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(32767),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="Возраст кота",
            ),
        ),
        migrations.AlterField(
            model_name="cat",
            name="name",
            field=models.CharField(
                max_length=100,
                validators=[cats.validator.NameValidator],
                verbose_name="Имя кота",
            ),
        ),
        migrations.AlterField(
            model_name="cat",
            name="weight",
            field=models.FloatField(
                validators=[
                    django.core.validators.MaxValueValidator(32767),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="Вес кота",
            ),
        ),
    ]
