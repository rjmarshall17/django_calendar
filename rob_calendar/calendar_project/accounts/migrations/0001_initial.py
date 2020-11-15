# Generated by Django 3.1.3 on 2020-11-14 18:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 11, 14, 18, 33, 26, 431287, tzinfo=utc))),
            ],
        ),
    ]