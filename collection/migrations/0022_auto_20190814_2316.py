# Generated by Django 2.2.3 on 2019-08-14 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0021_auto_20190814_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='firstname',
            new_name='Comments',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='lastname',
            new_name='Username',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='country',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='subject',
        ),
    ]