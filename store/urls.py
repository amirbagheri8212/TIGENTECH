from django.contrib.auth import views
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.mainp),
    url(r'^pagenum/?(?P<pagenum>[0-9]+)', views.page),
]
