from django.urls import path
from . import views


urlpatterns = [
    path('category/cardigan', views.cardigan_view, name='cardigan_index'),
    path('category/pullover', views.pullover_view, name='pullover_index'),
    path('category/vest', views.vest_view, name='vest_index'),
    path('category/gender/male', views.male_view, name='male_index'),
    path('category/gender/female', views.female_view, name='female_index'),
    path('category/gender/kids', views.kids_view, name='kids_index'),
]
