# Generated by Django 2.2.17 on 2021-03-15 15:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210315_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 17, 15, 43, 28, 134988, tzinfo=utc)),
        ),
    ]
