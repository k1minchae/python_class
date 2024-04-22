# Generated by Django 4.2.11 on 2024-04-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0002_author_subscribed_users'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribers', to='libraries.author'),
        ),
    ]