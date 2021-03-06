"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from account.views import custom_login, register
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^login/$',LoginView.as_view(redirect_authenticated_user=True, template_name='account/login.html'),name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout,
        {'template_name': 'account/logged_out.html'}, name='logout'),

    url(r'^admin/', admin.site.urls),
    url(r'^', include('ans.urls', namespace='ans')),
    url(r'^profile/', include('account.urls', namespace='account')),
]
