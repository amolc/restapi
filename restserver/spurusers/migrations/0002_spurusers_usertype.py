# Generated by Django 4.0.4 on 2022-04-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spurusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spurusers',
            name='usertype',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
