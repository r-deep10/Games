# Generated by Django 2.2.3 on 2019-09-02 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0025_delete_feedback2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='subject',
            new_name='comment',
        ),
    ]
