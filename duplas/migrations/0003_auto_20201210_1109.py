# Generated by Django 3.1.4 on 2020-12-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duplas', '0002_duplas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duplas',
            name='data',
            field=models.DateField(unique=True),
        ),
    ]