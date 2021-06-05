from django.conf.urls import url
from . import views


app_name='news'
urlpatterns = [
    url(r'^news/(?P<pk>\d+)/$', views.news_details, name='news-details'),
    url(r'^panel/news/list/$', views.news_list, name='news-list'),
    url(r'^panel/news/add/$', views.news_add, name='news-add'),
    url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news-delete'),
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news-edit'),
]
