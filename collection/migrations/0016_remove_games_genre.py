# Generated by Django 2.2.3 on 2019-07-22 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0015_auto_20190722_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='genre',
        ),
    ]
