# Generated by Django 2.2.3 on 2019-07-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20190711_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='action_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='adventure_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='arcade_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='competitive_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='fighting_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='horror_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='racing_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='shooting_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='sports_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='strategy_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='survival_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='top_trending',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='war_games',
            name='Game_id',
            field=models.CharField(default=123, max_length=20),
        ),
    ]