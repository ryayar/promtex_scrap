# Generated by Django 4.1.4 on 2022-12-16 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapproduct',
            name='query_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 11, 33, 25, 477827)),
        ),
    ]
