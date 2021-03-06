# Generated by Django 4.0.1 on 2022-03-23 02:07

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(blank=True, max_length=255, null=True, verbose_name='page')),
                ('image', models.ImageField(default='uploads/Content.png', upload_to=content.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
