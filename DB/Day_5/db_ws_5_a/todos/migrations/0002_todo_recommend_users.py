# Generated by Django 4.2.9 on 2024-04-08 02:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='recommend_users',
            field=models.ManyToManyField(related_name='recommend_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
