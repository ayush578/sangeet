# Generated by Django 4.2.3 on 2023-07-17 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_queue_pointer_alter_song_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='pointer',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 17, 4, 59, 8, 38122, tzinfo=datetime.timezone.utc)),
        ),
    ]
