# Generated by Django 2.2.3 on 2019-07-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0016_remove_games_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='requirement',
            field=models.CharField(default='-', max_length=1000),
        ),
    ]