from django.conf.urls import url
from . import views

app_name = 'MainPageApp'

urlpatterns = [
    url(r'^$', views.HomePage, name = 'HomePage'),
    url(r'^pagenum/?(?P<pagenum>[0-9]+)', views.HomePage1),
]