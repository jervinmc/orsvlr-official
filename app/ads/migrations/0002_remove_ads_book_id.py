# Generated by Django 4.0.1 on 2022-05-29 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='book_id',
        ),
    ]
