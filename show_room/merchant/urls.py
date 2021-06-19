from django.urls import path
from . import views


urlpatterns = [
    path('merchant/', views.index, name='merchant_index')
]
