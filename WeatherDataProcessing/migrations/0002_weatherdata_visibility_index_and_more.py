# Generated by Django 4.2.3 on 2023-08-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherDataProcessing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdata',
            name='visibility_index',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='heat_index',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='rainfall_index',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='wind_index',
            field=models.CharField(max_length=100),
        ),
    ]
