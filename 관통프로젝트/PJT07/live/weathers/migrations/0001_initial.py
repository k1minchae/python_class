# Generated by Django 4.2.11 on 2024-04-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_txt', models.DateTimeField()),
                ('temp', models.FloatField()),
                ('feels_like', models.FloatField()),
            ],
        ),
    ]
