from django.conf.urls import url
from . import views
app_name='ProgramSerieApp'
urlpatterns = [
    url(r'^$', views.productpage, name='ProgramSeriesPage'),
    url(r'^(?P<Product_id>[0-9]+)/$',views.detail,name='ProgramSerieDetail'),
    url(r'^(?P<Product_id>[0-9]+)/(?P<Program_id>[0-9]+)/$',views.programdetail,name="ProgramDetail")
    #url(r'register/^$', views.UserFormView.as_view(),name='register')
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)