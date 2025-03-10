# Generated by Django 5.1.1 on 2024-11-06 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hairstylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('experience_years', models.IntegerField()),
                ('specialization', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hairstyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default=None, null=True, upload_to='images')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('duration_minutes', models.IntegerField()),
                ('hairstyle_type', models.CharField(choices=[('men', 'Men'), ('women', 'Women'), ('hair_coloring', 'Hair Coloring'), ('hair_treatment', 'Hair Treatment')], max_length=15)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.hairstylist')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=20)),
                ('appointment_date', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('hairstyle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.hairstyle')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.hairstylist')),
            ],
        ),
    ]
