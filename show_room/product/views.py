from product.models import Product
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from category.models import Category
from django.db.models import Q


def index(request):
    products = Product.objects.all()
    return render(request, 'product/product.html', {'products': products})


def details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product/product_details.html', {'product': product})


# Search from navbar
class SearchResultView(ListView):
    model = Product
    template_name = 'product/search_result.html'

    def get_queryset(self):
        category = Category.objects.all()
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(product_style__icontains=query) | Q(product_composition__icontains=query) |
            Q(product_gauge__icontains=query) | Q(product_size__icontains=query) |
            Q(product_weight__icontains=query) | Q(product_moq__icontains=query) |
            Q(product_fob__icontains=query) | Q(product_category__category_name__icontains=query) |
            Q(product_gender__gender_name__icontains=query)
        )

        return object_list