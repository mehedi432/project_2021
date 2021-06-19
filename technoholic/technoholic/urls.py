from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "TECHNOHOLIC | ADMIN"
admin.site.site_title = "Technoholic Admin Portal"
admin.site.index_title = "Welcome to Technoholic Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


