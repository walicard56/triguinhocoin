from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tigrinho.urls')),  # Inclua as URLs do seu aplicativo
]
