from django.shortcuts import render
from .models import Article, Category, Tag


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/blog.html', {'articles': articles, 'categories': categories, 'tags': tags})


def details(request, pk):
    article = Article.objects.get(pk=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/blog-single.html', {'article': article, 'categories': categories, 'tags': tags})
