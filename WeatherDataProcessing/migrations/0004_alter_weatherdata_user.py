# Generated by Django 4.2.3 on 2023-08-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherDataProcessing', '0003_alter_weatherdata_heat_index_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdata',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]