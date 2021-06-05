# Building online news Portal

---

Part One - Site Settings
1. Starting new django project
2. Setting up path for main
3. Adding template magnews with static files
4. Adding all images
5. Make site settings from admin and dynamically add social links, footer part and header part

Part Two - Make News App
1. Make an app called news
2. Pull data from database to show latest news
3. Make news details page - incomplete (Need to change url text from number to word)

Part Three - Make Admin Panel
1. Add pro ui admin template for admin
2. Making admin page list news with datatables
3. Fetch data from database to view in datatables

Part Four - Make admin to add news from backend
1. Make frontend to take input from the user
2. Make form to validate if form is submittet blank or not
3. Save form data to database and show it in news-list admin panel

Part Five - Upload Files
1. Setup project to dynamically gather urls for static assets or images
2. How to save a file with generated url 
```py
    # models.py
    from django.db import models

    class Picture(models.Model):
        picture = models.TextField()
     
    # urls.py from generated project
    from django.conf import settings
    from django.conf.urls.static import static

    if setting.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    # settings.py
    MEDIA_ROOT = '/media/'
    MEDIA_URL = os.path.join(BASE_DIR, 'media')


    # views.py 
    from .models import Picture
    from django.core.files.storage import FileSystemStorage

    # Get the file from the frontend
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    url = fs.url(filename)
    # Picture is a model which now store image with generated url
    picture = Picture(picture=url)
```
3. Check for the correct file type as Image else send error to the user
4. Limit size of the image.

Part Six - Add datetime
1. Add date and time from the system
2. Automaticcaly add it to the database and show it

Part Seven - Delete a record of post 
1. Delete the post with associate Image file
2. Also delete uploaded other type of file

Part Eight - Category & SubCategory
1. Make a new app named as category
2. Category CRUD
3. Make Subcategory app
4. Make relation with category to subcategory
5. Add subcategory to our add news page

