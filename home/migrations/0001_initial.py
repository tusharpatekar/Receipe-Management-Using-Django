# Generated by Django 4.2.18 on 2025-01-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("file", models.FileField(upload_to="")),
            ],
        ),
    ]
