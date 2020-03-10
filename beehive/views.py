from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from beehive.forms import (ApiaryCreateForm,
                           BeeHiveCreateForm,
                           BeeFamilyCreateForm,
                           BeeMotherCreateForm)
from beehive.models import *


class IndexView(View):
    def get(self, request):
        return render(request, "pages/index.html")


class ApiaryListView(View):
    def get(self, request):
        apiary = Apiary.objects.all().order_by("id")
        return render(request, "pages/apiary_list_view.html", {"apiary": apiary})


class ApiaryView(View):
    def get(self, request, apiary_id):
        apiary = Apiary.objects.get(id=apiary_id)
        return render(request, "pages/apiary_view.html", {"apiary": apiary})


class BeeHiveListView(View):
    def get(self, request):
        beehive = BeeHive.objects.all().order_by("id")
        return render(request, "pages/beehive_list_view.html", {"beehive": beehive})


class BeeHiveView(View):
    def get(self, request, beehive_id):
        beehive = BeeHive.objects.get(id=beehive_id)
        return render(request, "pages/beehive_view.html", {"beehive": beehive})


class BeeFamilyListView(View):
    def get(self, request):
        beefamily = BeeFamily.objects.all().order_by("id")
        return render(request, "pages/beefamily_list_view.html", {"beefamily": beefamily})


class BeeFamilyView(View):
    def get(self, request, beefamily_id):
        beefamily = BeeFamily.objects.get(id=beefamily_id)
        return render(request, "pages/beefamily_view.html", {"beefamily": beefamily})


class BeeMotherListView(View):
    def get(self, request):
        beemother = BeeMother.objects.all()
        return render(request, "pages/beemother_list_view.html", {"beemother": beemother})


class BeeMotherView(View):
    def get(self, request, beemother_id):
        beemother = BeeMother.objects.get(id=beemother_id)
        return render(request, "pages/beemother_view.html", {"beemother": beemother})


class ApiaryCreateView(CreateView):
    template_name = 'forms/apiary_create_form.html'
    form_class = ApiaryCreateForm
    success_url = '/'


class BeeHiveCreateView(CreateView):
    template_name = 'forms/beehive_create_form.html'
    form_class = BeeHiveCreateForm
    success_url = '/'


class BeeFamilyCreateView(CreateView):
    template_name = 'forms/beefamily_create_form.html'
    form_class = BeeFamilyCreateForm
    success_url = '/'


class BeeMotherCreateView(CreateView):
    template_name = 'forms/beemother_create_form.html'
    form_class = BeeMotherCreateForm
    success_url = '/'

