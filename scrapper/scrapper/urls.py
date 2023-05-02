from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('fakebookScrapper.urls')),
    path('admin/', admin.site.urls),
]
