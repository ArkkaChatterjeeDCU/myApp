# Generated by Django 4.2.3 on 2023-08-13 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heat_index', models.CharField(choices=[('moderate', 'Moderate'), ('caution', 'Caution'), ('danger', 'Danger')], max_length=100)),
                ('wind_index', models.CharField(choices=[('light_breeze', 'Light Breeze'), ('moderate_breeze', 'Moderate Breeze'), ('strong_winds', 'Strong Winds'), ('storm_force_winds', 'Storm Force Winds')], max_length=100)),
                ('rainfall_index', models.CharField(choices=[('light_occasional_rain', 'Light & Occasional Rain'), ('moderate_rain', 'Moderate Rain'), ('heavy_rain', 'Heavy Rain'), ('torrential_rain', 'Torrential Rain')], max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
