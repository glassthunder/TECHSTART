# Generated by Django 3.0.5 on 2021-03-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='redirect_uri',
        ),
        migrations.AddField(
            model_name='apiinfo',
            name='redirect_u',
            field=models.CharField(default='', max_length=500),
        ),
    ]