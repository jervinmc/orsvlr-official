# Generated by Django 4.0.1 on 2022-05-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_alter_book_checkin_time_alter_book_checkout_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ad_other',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ad_other'),
        ),
        migrations.AddField(
            model_name='book',
            name='ad_other_total',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ad_other_total'),
        ),
    ]