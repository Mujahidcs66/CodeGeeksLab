# Generated by Django 4.2.6 on 2023-11-05 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='img',
            field=models.ImageField(upload_to='images/%Y/'),
        ),
        migrations.AlterField(
            model_name='geeksmodel',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
