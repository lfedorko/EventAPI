# Generated by Django 2.1.4 on 2018-12-15 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='photo',
            new_name='place',
        ),
    ]