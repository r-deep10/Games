from django.contrib import admin
from collection.models import Games, Feedback


class GamesAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'gname', 'publisher', 'release_date', 'game_id',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'firstname', 'country')


admin.site.site_header = '--GAME HUB--'
admin.site.register(Games, GamesAdmin)
admin.site.register(Feedback, FeedbackAdmin)
