from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += staticfiles_urlpatterns()