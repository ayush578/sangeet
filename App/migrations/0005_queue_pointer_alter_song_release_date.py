# Generated by Django 4.2.3 on 2023-07-16 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_song_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='pointer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 16, 11, 53, 44, 372435, tzinfo=datetime.timezone.utc)),
        ),
    ]
