# Generated by Django 3.2.3 on 2021-05-22 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='new_url',
            new_name='short_url_code',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='old_url',
            new_name='url',
        ),
    ]
