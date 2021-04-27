# Generated by Django 3.0.5 on 2021-04-26 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiInfo',
            fields=[
                ('api_name', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('client_id', models.CharField(default='N/A', max_length=100)),
                ('secret', models.CharField(max_length=100)),
                ('base_url', models.CharField(max_length=2083, unique=True)),
                ('api_endpoint', models.CharField(default='N/A', max_length=2083)),
                ('token_endpoint', models.CharField(max_length=2083)),
                ('redirect_url', models.CharField(default='', max_length=500)),
                ('scope', jsonfield.fields.JSONField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DiscordAPIInfo',
            fields=[
                ('apiinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrations.ApiInfo')),
            ],
            bases=('integrations.apiinfo',),
        ),
        migrations.CreateModel(
            name='NewsApiInfo',
            fields=[
                ('apiinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrations.ApiInfo')),
            ],
            bases=('integrations.apiinfo',),
        ),
        migrations.CreateModel(
            name='OutlookAPIInfo',
            fields=[
                ('apiinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrations.ApiInfo')),
            ],
            bases=('integrations.apiinfo',),
        ),
        migrations.CreateModel(
            name='RedditAPIInfo',
            fields=[
                ('apiinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrations.ApiInfo')),
            ],
            bases=('integrations.apiinfo',),
        ),
        migrations.CreateModel(
            name='SpotifyAPIInfo',
            fields=[
                ('apiinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrations.ApiInfo')),
            ],
            bases=('integrations.apiinfo',),
        ),
        migrations.CreateModel(
            name='Spotify_User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_user_name', models.CharField(default='', max_length=30)),
                ('user_id', models.CharField(max_length=10)),
                ('token', models.CharField(default='', max_length=2048)),
                ('refresh_token', models.CharField(blank=True, max_length=512)),
                ('token_type', models.CharField(blank=True, max_length=10)),
                ('expires_in', models.CharField(blank=True, max_length=60)),
                ('expires_at', models.CharField(blank=True, max_length=100)),
                ('account_name', models.CharField(default='spotify', editable=False, max_length=7)),
                ('users', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reddit_User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_user_name', models.CharField(default='', max_length=30)),
                ('user_id', models.CharField(max_length=10)),
                ('token', models.CharField(default='', max_length=2048)),
                ('refresh_token', models.CharField(blank=True, max_length=512)),
                ('token_type', models.CharField(blank=True, max_length=10)),
                ('expires_in', models.CharField(blank=True, max_length=60)),
                ('expires_at', models.CharField(blank=True, max_length=100)),
                ('account_name', models.CharField(default='reddit', editable=False, max_length=6)),
                ('users', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Outlook_User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_user_name', models.CharField(default='', max_length=30)),
                ('user_id', models.CharField(max_length=10)),
                ('token', models.CharField(default='', max_length=2048)),
                ('refresh_token', models.CharField(blank=True, max_length=512)),
                ('token_type', models.CharField(blank=True, max_length=10)),
                ('expires_in', models.CharField(blank=True, max_length=60)),
                ('expires_at', models.CharField(blank=True, max_length=100)),
                ('account_name', models.CharField(default='outlook', editable=False, max_length=7)),
                ('users', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News_User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_user_name', models.CharField(default='', max_length=30)),
                ('user_id', models.CharField(max_length=10)),
                ('token', models.CharField(default='', max_length=2048)),
                ('refresh_token', models.CharField(blank=True, max_length=512)),
                ('token_type', models.CharField(blank=True, max_length=10)),
                ('expires_in', models.CharField(blank=True, max_length=60)),
                ('expires_at', models.CharField(blank=True, max_length=100)),
                ('account_name', models.CharField(default='newsapi', editable=False, max_length=7)),
                ('preferences', models.CharField(default='', max_length=100)),
                ('users', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discord_User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_user_name', models.CharField(default='', max_length=30)),
                ('user_id', models.CharField(max_length=10)),
                ('token', models.CharField(default='', max_length=2048)),
                ('refresh_token', models.CharField(blank=True, max_length=512)),
                ('token_type', models.CharField(blank=True, max_length=10)),
                ('expires_in', models.CharField(blank=True, max_length=60)),
                ('expires_at', models.CharField(blank=True, max_length=100)),
                ('account_name', models.CharField(default='discord', editable=False, max_length=7)),
                ('users', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
