# Generated by Django 3.1.4 on 2020-12-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duplas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duplas',
            name='data',
            field=models.DateField(default='2020-12-8'),
            preserve_default=False,
        ),
    ]