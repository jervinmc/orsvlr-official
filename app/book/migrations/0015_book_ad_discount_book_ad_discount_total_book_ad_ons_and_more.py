# Generated by Django 4.0.1 on 2022-05-29 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_book_date_reschedule_book_reason_reschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ad_discount',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ad_discount'),
        ),
        migrations.AddField(
            model_name='book',
            name='ad_discount_total',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ad_ons_total'),
        ),
        migrations.AddField(
            model_name='book',
            name='ad_ons',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ad_ons'),
        ),
        migrations.AddField(
            model_name='book',
            name='ad_ons_total',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ad_ons_total'),
        ),
    ]