# Generated by Django 3.1.3 on 2020-11-15 04:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201114_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='email',
            new_name='user_email',
        ),
        migrations.AlterField(
            model_name='account',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 4, 21, 48, 257732, tzinfo=utc)),
        ),
    ]
