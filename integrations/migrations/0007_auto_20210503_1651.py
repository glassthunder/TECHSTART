# Generated by Django 3.0.5 on 2021-05-03 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0006_news_user_info_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlook_user_info',
            name='authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reddit_user_info',
            name='authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='spotify_user_info',
            name='authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
