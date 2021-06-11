from django.urls import path
from . import views


app_name='product'
urlpatterns = [
    path('', views.index, name='product_index'),
    path('product/<int:id>', views.details, name='product_details'),
    path("search/", views.SearchResultView.as_view(), name='search'),
]
