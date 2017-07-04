from django.contrib.auth import views
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.mainp),
    url(r'^(?P<genrepk>[0-9]+)/(?P<postpk>[0-9]+)/', views.postdet),
    url(r'^(?P<genrepk>[0-9]+)/', views.genredet),
]
