from django.shortcuts import render
from django.db.models import Q
from product.models import Product


def cardigan_view(request):
    query = 'cardigan'
    cardigans = Product.objects.filter(
        Q(product_category__category_name__exact=query)
    )
    return render(request, 'product/core/cardigan/cardigan_list.html', {'products': cardigans})


def pullover_view(request):
    query = 'pullover'
    pullover = Product.objects.filter(
        Q(product_category__category_name__exact=query)
    )
    return render(request, 'product/core/pullover/pullover_list.html', {'products': pullover})


def vest_view(request):
    query = 'vest'
    vest = Product.objects.filter(
        Q(product_category__category_name__exact=query)
    )
    return render(request, 'product/core/vest/vest_list.html', {'products': vest})


def male_view(request):
    query = 'male'
    male = Product.objects.filter(
        Q(product_gender__gender_name__exact=query)
    )
    return render(request, 'product/core/gender/male_list.html', {'products': male})


def female_view(request):
    query = 'female'
    female = Product.objects.filter(
        Q(product_gender__gender_name__exact=query)
    )
    return render(request, 'product/core/gender/female_list.html', {'products': female})


def kids_view(request):
    query = 'kids'
    kids = Product.objects.filter(
        Q(product_gender__gender_name__exact=query)
    )
    return render(request, 'product/core/gender/kids_list.html', {'products': kids})