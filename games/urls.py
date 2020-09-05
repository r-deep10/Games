"""games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from collection import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.trend),
    path('4/', views.game, name='game_home'),
    path('5/',views.all),
    path('1/', views.fetch),
    path('2/', views.feedback),
    path('3/', views.abc4),
    re_path('details/', include('collection.url')),
    re_path('search/$', views.search, name='search'),
    
]
