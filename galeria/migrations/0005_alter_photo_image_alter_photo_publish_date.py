# Generated by Django 5.1 on 2024-08-28 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_photo_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 28, 18, 42, 57, 498579)),
        ),
    ]
