from django.conf.urls import url
from . import views


app_name = 'subcategory'
urlpatterns = [
    url(r'^panel/subcategory/add/$', views.subcategory_add, name='subcategory-add'),
    url(r'^panel/subcategory/list/$', views.subcategory_list, name='subcategory-list'),
]
