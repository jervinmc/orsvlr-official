# Generated by Django 4.0.1 on 2022-06-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_pend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adpend',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='quantity'),
        ),
    ]
