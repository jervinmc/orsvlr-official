# Generated by Django 4.0 on 2022-01-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='code'),
        ),
        migrations.AddField(
            model_name='book',
            name='mode_of_payment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='mode_of_payment'),
        ),
    ]
