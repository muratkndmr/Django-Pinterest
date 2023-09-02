"""
URL configuration for staj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from giris.views import *
from user.views import *

urlpatterns = [
    path('',indexPage,name='index'),
    path('admin/', admin.site.urls),
    path('anasayfa', anasayfa, name='anasayfa'),
    path('busines', busines, name='busines'),
    path('profile', profile, name='profile'),
    path('setting', setting, name='setting'),
    path('account', account, name='account'),
    path('profiVisibility', profiVisibility, name='profiVisibility'),
    path('history', history, name='history'),
    path('claim', claim, name='claim'),
    path('permissions', permissions, name='permissions'),
    path('notifications', notifications, name='notifications'),
    path('privacy', privacy, name='privacy'),
    path('security', security, name='security'),
    path('brand', brand, name='brand'),
    path('addAccount', addAccount, name='addAccount'),
    path('inNavbar', inNavbar, name='inNavbar'),
    path('logout', logoutUser, name='logoutUser'),
    path('comments', comments, name='comments')








] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

