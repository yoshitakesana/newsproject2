# Generated by Django 4.2 on 2025-01-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp2', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
