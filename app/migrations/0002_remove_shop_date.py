# Generated by Django 4.0 on 2023-01-07 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='date',
        ),
    ]