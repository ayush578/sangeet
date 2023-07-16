# Generated by Django 4.2.3 on 2023-07-16 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 16, 6, 12, 0, 488712, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shuffle', models.BooleanField(default=False)),
                ('repeat', models.BooleanField(default=False)),
                ('songs', models.ManyToManyField(to='App.song')),
            ],
        ),
    ]