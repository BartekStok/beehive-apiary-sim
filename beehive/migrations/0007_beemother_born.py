# Generated by Django 2.2.7 on 2020-03-11 21:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beehive', '0006_auto_20200311_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='beemother',
            name='born',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 11, 21, 16, 20, 927603, tzinfo=utc)),
        ),
    ]
