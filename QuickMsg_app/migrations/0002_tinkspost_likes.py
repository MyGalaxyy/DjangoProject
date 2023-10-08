# Generated by Django 4.2.3 on 2023-09-26 23:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickMsg_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tinkspost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_like', to=settings.AUTH_USER_MODEL),
        ),
    ]