from django.db import models


class Games(models.Model):
    gname = models.CharField(default='a', max_length=100)
    category = models.CharField(default='-', max_length=250)
    language = models.CharField(default='English', max_length=250)
    requirement = models.TextField(default='-')
    release_date = models.CharField(default='-', max_length=250)
    publisher = models.CharField(default='-', max_length=250)
    platforms = models.CharField(default='-', max_length=250)
    summery = models.TextField(default='-')
    screenshot = models.CharField(default='-', max_length=500)
    screenshot1 = models.CharField(default='-', max_length=500)
    screenshot2 = models.CharField(default='-', max_length=500)
    screenshot3 = models.CharField(default='-', max_length=500)
    screenshot4 = models.CharField(default='-', max_length=500)
    screenshot5 = models.CharField(default='-', max_length=500)
    game_id = models.CharField(default='game', max_length=250)
    game_img = models.CharField(max_length=100, default='0')
    download_link = models.CharField(default='-', max_length=500)

    def __str__(self):
        return self.gname


class Feedback(models.Model):
    firstname = models.CharField(max_length=100, default='-')
    lastname = models.CharField(max_length=100, default='-')
    country = models.CharField(max_length=50, default='-')
    comment = models.TextField(default='-')

    def __str__(self):
        return self.comment
