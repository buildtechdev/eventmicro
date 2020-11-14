# Generated by Django 3.1.1 on 2020-11-14 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20201114_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.course')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.event')),
            ],
        ),
        migrations.DeleteModel(
            name='CourseSession',
        ),
    ]
