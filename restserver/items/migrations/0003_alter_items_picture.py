# Generated by Django 4.0.4 on 2022-05-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_items_thumbnailimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.TextField(blank=True),
        ),
    ]