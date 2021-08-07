# Generated by Django 3.1.4 on 2021-08-07 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duplas', '0005_duplas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True, verbose_name='Data')),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Nome')),
                ('surname', models.CharField(blank=True, max_length=127, null=True, verbose_name='Sobrenome')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20, verbose_name='Sexo')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
        ),
        migrations.DeleteModel(
            name='Duplas',
        ),
        migrations.DeleteModel(
            name='Integrante',
        ),
        migrations.AddField(
            model_name='duos',
            name='member_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_member', to='duplas.members'),
        ),
        migrations.AddField(
            model_name='duos',
            name='member_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_member', to='duplas.members'),
        ),
    ]
