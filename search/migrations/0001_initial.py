# Generated by Django 3.1.6 on 2021-02-25 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("brands", models.CharField(max_length=150)),
                ("barcode", models.CharField(max_length=13, unique=True)),
                ("nutriscore", models.CharField(max_length=1)),
                ("url", models.URLField()),
                ("image_url", models.URLField()),
                ("image_small_url", models.URLField()),
                ("energy_100g", models.FloatField(default=0, null=True)),
                ("sugars_100g", models.FloatField(default=0, null=True)),
                ("sodium_100g", models.FloatField(default=0, null=True)),
                ("fat_100g", models.FloatField(default=0, null=True)),
                ("salt_100g", models.FloatField(default=0, null=True)),
                ("categories", models.ManyToManyField(to="search.Category")),
            ],
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorite_product",
                        to="search.product",
                    ),
                ),
                (
                    "substitute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorite_substitute",
                        to="search.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorite_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
