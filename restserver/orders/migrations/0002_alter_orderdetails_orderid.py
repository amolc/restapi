# Generated by Django 4.0.4 on 2022-05-20 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='orderid',
            field=models.PositiveIntegerField(),
        ),
    ]