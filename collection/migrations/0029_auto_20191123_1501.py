# Generated by Django 2.2.6 on 2019-11-23 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0028_auto_20191118_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='lastname',
            new_name='email',
        ),
    ]