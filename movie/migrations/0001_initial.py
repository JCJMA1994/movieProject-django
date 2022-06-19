# Generated by Django 4.0 on 2022-06-18 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=70)),
                ('date_birth', models.DateField()),
                ('date_death', models.DateField(blank=True, null=True)),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('synopsis', models.TextField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.director')),
            ],
        ),
    ]