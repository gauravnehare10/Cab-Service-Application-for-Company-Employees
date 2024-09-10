"""
URL configuration for transport project.

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
from cabservice.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', registerview, name='register'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('emp_prof/', emp_profile, name='emp_prof'),
    path('update_profile/', update_profile, name='update_profile'),
    path('book/', booking, name='book'),
    path('mybookings/', mybooking_view, name='mybookings'),
    path('book_history/', book_history, name='book_history'),
    path('cabdetail/<int:id>', cabdetail_view, name='cabdetail'),
]
