from django.shortcuts import redirect, render
from .models import SubCategory
from category.models import Category


# Create your views here.
def subcategory_list(request):
    subcategory = SubCategory.objects.all()
    return render(request, 'back/subcategory_list.html', {'subcategory':subcategory})


def subcategory_add(request):

    category = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get('subcategory_name')
        category_id = request.POST.get('newscat')

        if name == "":
            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})

        try:
            if (SubCategory.objects.get(name=name)) != 0:
                error = "This category already exists."
                return render(request, 'back/error.html', {'error': error})
        except SubCategory.DoesNotExist:
            pass
        
        try:
            category_name = Category.objects.get(pk=category_id).name
        except Category.DoesNotExist:
            category_name = None

        subcategory = SubCategory(name=name, category_name=category_name, category_id=category_id)
        subcategory.save()

        return redirect('subcategory:subcategory-list')
    return render(request, 'back/subcategory_add.html', {'category': category})