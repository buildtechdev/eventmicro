# Generated by Django 3.1.1 on 2020-12-16 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20201119_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='reminder_on',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]