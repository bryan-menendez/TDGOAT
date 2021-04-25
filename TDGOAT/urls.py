"""TDGOAT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from lists import views as listviews

urlpatterns = [
    path('', listviews.index),
    path('lists/new', listviews.new_list, name="new_list"),
    path('lists/the-one-and-only-forever-and-ever-till-the-end-of-time', listviews.view_list, name="view_list"),
    path('admin/', admin.site.urls),
]
