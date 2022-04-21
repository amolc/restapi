# Generated by Django 4.0.4 on 2022-04-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgName', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('userPhone', models.CharField(max_length=200)),
                ('demoOrgID', models.CharField(blank=True, max_length=200, null=True)),
                ('demo_key', models.CharField(blank=True, max_length=200, null=True)),
                ('demo_value', models.CharField(blank=True, max_length=200, null=True)),
                ('live_key', models.CharField(blank=True, max_length=200, null=True)),
                ('live_value', models.CharField(blank=True, max_length=200, null=True)),
                ('liveOrgID', models.CharField(blank=True, max_length=200, null=True)),
                ('paymentID', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
