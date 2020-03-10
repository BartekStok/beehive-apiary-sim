"""apiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from beehive.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="home"),
    path('apiary_create/', ApiaryCreateView.as_view(), name="apiary-create-form"),
    path('beehive_create/', BeeHiveCreateView.as_view(), name="beehive-create-form"),
    path('beefamily_create/', BeeFamilyCreateView.as_view(), name="beefamily-create-form"),
    path('beemother_create/', BeeMotherCreateView.as_view(), name="beemother-create-form"),
]
