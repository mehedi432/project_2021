from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<int:pk>/', views.details, name='blog_details'),

]
