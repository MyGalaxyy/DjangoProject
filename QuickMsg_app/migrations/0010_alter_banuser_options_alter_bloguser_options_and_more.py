# Generated by Django 4.2.3 on 2023-10-04 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickMsg_app', '0009_alter_removeban_authorizeduser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banuser',
            options={'verbose_name': 'Banli Kullanici', 'verbose_name_plural': 'Banlanan Kullanicilar'},
        ),
        migrations.AlterModelOptions(
            name='bloguser',
            options={'verbose_name': 'Kullanici', 'verbose_name_plural': 'Kullanicilar'},
        ),
        migrations.AlterModelOptions(
            name='removeban',
            options={'verbose_name': 'Bani Kaldirilan Kullanici', 'verbose_name_plural': 'Bani Kaldirilan Kullanicilar'},
        ),
        migrations.AlterModelOptions(
            name='reportmanagement',
            options={'verbose_name': 'Şikayet Edilen Kullanici', 'verbose_name_plural': 'Şikayet Edilen Kullanicilar'},
        ),
        migrations.AlterModelOptions(
            name='tinkspost',
            options={'verbose_name': 'Tweet', 'verbose_name_plural': 'Kullanici Tweetleri'},
        ),
        migrations.AlterModelOptions(
            name='tweetcomment',
            options={'verbose_name': 'Yorum', 'verbose_name_plural': ' Kullanici Yorumlari'},
        ),
    ]
