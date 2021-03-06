# Generated by Django 4.0.1 on 2022-06-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdPend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='price')),
                ('label', models.CharField(blank=True, max_length=255, null=True, verbose_name='label')),
                ('book_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='book_id')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
