# Generated by Django 3.1.3 on 2020-11-15 12:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201115_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 12, 34, 31, 757850, tzinfo=utc)),
        ),
    ]