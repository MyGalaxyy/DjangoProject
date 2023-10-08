# Generated by Django 4.2.3 on 2023-10-01 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuickMsg_app', '0007_alter_banuser_banreason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banuser',
            name='banReason',
            field=models.TextField(default=None, max_length=100, verbose_name='Sebep:'),
        ),
        migrations.CreateModel(
            name='RemoveBan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removebanReason', models.TextField(default=None, max_length=100, verbose_name='Sebep:')),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('authorizedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorized', to=settings.AUTH_USER_MODEL, verbose_name='Banlayan Yetkili:')),
                ('removedbanUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Bani Kaldirilan User:')),
            ],
        ),
    ]