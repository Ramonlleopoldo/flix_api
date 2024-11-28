# Generated by Django 5.1.3 on 2024-11-28 01:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_reviewmodels_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodels',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
