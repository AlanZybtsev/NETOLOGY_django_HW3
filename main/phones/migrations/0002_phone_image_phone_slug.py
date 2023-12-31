# Generated by Django 4.2.4 on 2023-10-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.URLField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
