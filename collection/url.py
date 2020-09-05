from django.contrib import admin
from django.urls import path,re_path,include
from collection import views

urlpatterns = [

re_path('(?P<gameid>[0-9]{3})', views.fetch),
re_path('(?P<general>[0-9a-zA-Z]+)',views.filt),


]