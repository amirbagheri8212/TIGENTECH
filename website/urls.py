"""website URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views
from accountmanagement import views as core_views
from accountmanagement.forms import LoginForm
from django.shortcuts import render
from django.contrib import admin
def construct(request):
    return render(request, 'costruct.html', {})
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include(admin.site.urls)),
    url(r'^', include('mainpage.urls', namespace='MainPage')),
    url(r'^teach/', include('teachprogramming.urls')),

    url(r'^programseries/', include('programseries.urls', namespace='ProgramSeriesUrl')),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$', views.login, {'template_name': 'accountmanagement/login.html', 'authentication_form': LoginForm},name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'},name='logout'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', core_views.activate,
        name='activate'),
    url(r'^construct/', construct),
    url(r'^store/', include("store.urls")),
    url(r'^posts/', include("posts.urls")),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)