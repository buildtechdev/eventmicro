# Generated by Django 3.1.1 on 2020-11-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_coursesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]