from django.conf.urls import url
from . import views


app_name = 'category'
urlpatterns = [
    url(r'^panel/category/add/$', views.category_add, name='category-add'),
    url(r'^panel/category/list/$', views.category_list, name='category-list'),
]
