# Generated by Django 4.0.3 on 2022-04-19 07:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 7, 11, 30, 161717, tzinfo=utc), help_text='The date the user joined Duwin.'),
        ),
    ]
