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
    path('apiary_view/', ApiaryListView.as_view(), name="apiary-list-view"),
    path('apiary_view/<int:apiary_id>', ApiaryView.as_view(), name="apiary-view"),
    path('apiary_update/<pk>/', ApiaryUpdateView.as_view(), name="apiary-update-form"),
    path('apiary_delete/<pk>/', ApiaryDeleteView.as_view(), name="apiary-delete-form"),
    path('beehive_create/', BeeHiveCreateView.as_view(), name="beehive-create-form"),
    path('beehive_view/', BeeHiveListView.as_view(), name="beehive-list-view"),
    path('beehive_view/<int:beehive_id>', BeeHiveView.as_view(), name="beehive-view"),
    path('beehive_update/<pk>', BeeHiveUpdateView.as_view(), name="beehive-update-form"),
    path('beehive_delete/<pk>', BeeHiveDeleteView.as_view(), name="beehive-delete-form"),
    path('beehive_service/<pk>', BeeHiveMakeService.as_view(), name="beehive-make-service"),
    path('beehive_take_honey/<pk>', BeeHiveTakeHoney.as_view(), name="beehive-take-honey"),
    path('beefamily_create/', BeeFamilyCreateView.as_view(), name="beefamily-create-form"),
    path('beefamily_view/', BeeFamilyListView.as_view(), name="beefamily-list-view"),
    path('beefamily_view/<int:beefamily_id>', BeeFamilyView.as_view(), name="beefamily-view"),
    path('beemother_create/', BeeMotherCreateView.as_view(), name="beemother-create-form"),
    path('beemother_view/', BeeMotherListView.as_view(), name="beemother-list-view"),
    path('beemother_view/<int:beemother_id>', BeeMotherView.as_view(), name="beemother-view"),
    path('dashboard/', DashboardService.as_view(), name="dashboard")
]
