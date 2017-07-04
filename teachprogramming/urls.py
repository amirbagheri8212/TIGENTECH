from django.conf.urls import url
from . import views
app_name='Teach'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<Language>[0-9]+)/$',views.teach,name='teach'),
    url(r'^(?P<Language>[a-zA-Z0-9]+)/(?P<TUT>[0-9]+)/$', views.TTutorial)
    #url(r'^(?P<Product_id>[0-9]+)/$',views.detail,name='productdetail'),
    #url(r'^(?P<Product_id>[0-9]+)/(?P<Program_id>[0-9]+)/$',views.programdetail,name="ProgramDetail")
    #url(r'register/^$', views.UserFormView.as_view(),name='register')
]