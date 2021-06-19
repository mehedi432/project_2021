from django.shortcuts import render
from .models import Merchant


def index(request):
    merchants = Merchant.objects.all()
    return render(request, 'product/merchant/index.html', {'merchants': merchants})