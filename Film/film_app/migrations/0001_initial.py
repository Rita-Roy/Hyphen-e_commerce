# Generated by Django 5.1.1 on 2024-11-06 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_date', models.DateField()),
                ('show_time', models.TimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film_app.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('is_available', models.BooleanField(default=True)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film_app.showtime')),
            ],
        ),
    ]
