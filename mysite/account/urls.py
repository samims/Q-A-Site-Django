from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from .views import profile

urlpatterns = [
    # /
    # url(r'^$', views.home),
    url(r'$', profile, name='profile')
    
]
