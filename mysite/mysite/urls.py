"""mysite URL Configuration
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from magasin import views
from . import views
from film import views
from . import views


urlpatterns = [
    path('',views.accueil),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
    path('film/', include('film.urls')),
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
