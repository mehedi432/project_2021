from django.shortcuts import render,  get_object_or_404, redirect
from .models import News
from django.core.files.storage import FileSystemStorage
import datetime
from subcategory.models import SubCategory


def news_details(request, pk):
    news = News.objects.filter(pk=pk)
    return render(request, 'front/main/news_details.html', {'news': news})


def news_list(request):
    news = News.objects.all()
    return render(request, 'back/news_list.html', {'news': news})
    

def news_add(request):
    
    # Handling datetime for the post
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(str(day)) == 1:
        day = "0" + str(day)

    today = str(day) + "/" + str(month) + "/" + str(year)
    today_time = str(hour) + ":" + str(minute)
    

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxtlong = request.POST.get('newstxtlong')
        news_id = request.POST.get('newscat')


        if newstitle == "" or newscat == "" or newstxtshort == "" or newstxtlong == "":
            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})
        
        try:
            # For storing file with url with unique name
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            # Check file is an image and the size is less than 5MB
            if str(myfile.content_type).startswith('image'):

                if myfile.size < 500000:

                    newsname = SubCategory.objects.get(pk=news_id).name
                    
                    news = News(name=newstitle, short_text=newstxtshort, long_text=newstxtlong, category=newsname, category_id=news_id, views=0, publish_date=today, publish_time=today_time, picture_name=filename, picture_url=url, writer='Admin')
                    news.save()
                    return redirect('news:news-list')

                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "File size is too big of your image."
                    return render(request, 'back/error.html', {'error': error})
            
            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "File type is not supported please input an image."
                return render(request, 'back/error.html', {'error': error})
        
        except:
            error = "Picture is required ! Image is an important one."
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/news_add.html', {'subcategory': SubCategory.objects.all()})


def news_delete(request, pk):

    try:
        news = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(news.picture_name)
        news.delete()

    except:
        error = "An error happened while removing post."
        return render(request, 'back/error.html', {'error': error})

    return redirect('news:news-list')



def news_edit(request, pk):
    if len(News.objects.filter(pk=pk)) == 0:
        error = "No news found with this primary key."
        return render(request, 'back/error.html', {'error': error})

    news = News.objects.get(pk=pk)
    subcategory = SubCategory.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxtlong = request.POST.get('newstxtlong')
        news_id = request.POST.get('newscat')


        if newstitle == "" or newscat == "" or newstxtshort == "" or newstxtlong == "":
            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})
        
        try:
            # For storing file with url with unique name
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            # Check file is an image and the size is less than 5MB
            if str(myfile.content_type).startswith('image'):

                if myfile.size < 500000:

                    newsname = SubCategory.objects.get(pk=news_id).name
                    
                    # If the image is changed delete the previous
                    fss = FileSystemStorage()
                    fss.delete(news.picture_name)

                    news = News.objects.get(pk=pk)
                    news.name = newstitle
                    news.short_text = newstxtshort
                    news.long_text = newstxtlong
                    news.category = newsname
                    news.category_id = news_id
                    news.picture_name = filename
                    news.picture_url = url
                    news.writer = '-'
                    news.save()
                    return redirect('news:news-list')

                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "File size is too big of your image."
                    return render(request, 'back/error.html', {'error': error})
            
            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "File type is not supported please input an image."
                return render(request, 'back/error.html', {'error': error})
        
        except:
            newsname = SubCategory.objects.get(pk=news_id).name
            
            news = News.objects.get(pk=pk)
            news.name = newstitle
            news.short_text = newstxtshort
            news.long_text = newstxtlong
            news.category = newsname
            news.category_id = news_id

            news.save()

            return redirect('news:news-list')


    return render(request, 'back/news_edit.html', {'pk':pk, 'news':news, 'subcategory':subcategory})