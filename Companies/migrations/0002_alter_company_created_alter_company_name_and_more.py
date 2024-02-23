# Generated by Django 5.0.2 on 2024-02-23 20:10

import Utils.slug
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Companies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="company",
            name="name",
            field=models.CharField(
                db_index=True, max_length=255, unique=True, verbose_name="Компания"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="slug",
            field=Utils.slug.AutoSlugField(
                populate_from="name", unique=True, verbose_name="Ссылка"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
        ),
    ]
