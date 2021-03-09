# Generated by Django 3.1.7 on 2021-03-09 01:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0003_auto_20210309_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='_twitteruser_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]