# Generated by Django 4.0.4 on 2022-04-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supercategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
