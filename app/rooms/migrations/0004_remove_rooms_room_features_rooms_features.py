# Generated by Django 4.0.1 on 2022-02-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_rooms_room_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='room_features',
        ),
        migrations.AddField(
            model_name='rooms',
            name='features',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='features'),
        ),
    ]