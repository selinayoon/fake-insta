# Generated by Django 2.1.8 on 2019-04-15 01:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
