"""
URL configuration for insta_clone_pr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from insta_clone_pr.views import *
from django.conf.urls.static import static
from django.conf import  settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',login_main,name="index"),
    path('home/',index,name='home'),
    path('register/',register,name='register'),
    path('upload/',upload,name='upload'),
    path('logout/',logout_main,name="logout"),
    
    
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

