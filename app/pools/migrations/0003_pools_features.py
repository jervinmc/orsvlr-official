# Generated by Django 4.0.1 on 2022-02-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0002_pools_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='pools',
            name='features',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='features'),
        ),
    ]