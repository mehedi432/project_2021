from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News


def index(request):
    site = Main.objects.all()
    news = News.objects.all()
    return render(request, 'front/main/index.html', {'site': site, 'news': news})


def panel(request):
    return render(request, 'back/index.html')


def about(request):
    return render(request, 'front/main/about.html')
