from django.shortcuts import redirect, render
from .models import Category


# Create your views here.
def category_list(request):
    category = Category.objects.all()
    return render(request, 'back/category_list.html', {'category':category})


def category_add(request):
    if request.method == "POST":
        name = request.POST.get('category_name')

        if name == "":
            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})
        try:
            if (Category.objects.get(name=name)) != 0:
                error = "This category already exists."
                return render(request, 'back/error.html', {'error': error})
        except Category.DoesNotExist:
            pass
        
        category = Category(name=name)
        category.save()

        return redirect('category:category-list')
    return render(request, 'back/category_add.html')