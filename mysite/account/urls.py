from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from .views import register

urlpatterns = [
    # /
    # url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'account/logged_out.html'}, name='logout'),
    url(r'^register/$', register, name='register'),
]
