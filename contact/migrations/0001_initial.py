# Generated by Django 5.0.4 on 2024-05-04 00:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
