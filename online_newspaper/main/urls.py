from django.conf.urls import url
from . import views


app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='main-index'),
    url(r'^panel/$', views.panel, name='admin-panel'),
    url(r'^about/$', views.about, name='main-about'),
]
