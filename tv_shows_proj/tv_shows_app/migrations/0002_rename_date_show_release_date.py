# Generated by Django 5.0.7 on 2024-07-12 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='date',
            new_name='release_date',
        ),
    ]