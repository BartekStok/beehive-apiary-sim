from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from beehive.forms import (ApiaryCreateForm,
                           BeeHiveCreateForm,
                           BeeFamilyCreateForm,
                           BeeMotherCreateForm)
from beehive.models import *
from beehive.service.bee_mother_service import *


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


class ApiaryUpdateView(UpdateView):
    model = Apiary
    form_class = ApiaryCreateForm
    template_name = "forms/apiary_update_form.html"
    success_url = reverse_lazy("apiary-list-view")


class ApiaryDeleteView(DeleteView):
    model = Apiary
    template_name = "forms/apiary_delete_form.html"
    success_url = reverse_lazy("apiary-list-view")


class BeeHiveCreateView(CreateView):
    template_name = 'forms/beehive_create_form.html'
    form_class = BeeHiveCreateForm
    success_url = '/'


class BeeHiveUpdateView(UpdateView):
    model = BeeHive
    form_class = BeeHiveCreateForm
    template_name = "forms/beehive_update_form.html"
    success_url = reverse_lazy("beehive-list-view")


class BeeHiveDeleteView(DeleteView):
    model = BeeHive
    template_name = "forms/beehive_delete_form.html"
    success_url = reverse_lazy("beehive-list-view")


class BeeHiveMakeService(View):
    def get(self, request, beehive_id):
        beehive = BeeHive.objects.get(id=beehive_id)
        beehive.service_date = timezone.now()
        return redirect(f'/beehive_view/{beehive_id}')


class BeeFamilyCreateView(CreateView):
    template_name = 'forms/beefamily_create_form.html'
    form_class = BeeFamilyCreateForm
    success_url = '/'


class BeeMotherCreateView(CreateView):
    template_name = 'forms/beemother_create_form.html'
    form_class = BeeMotherCreateForm
    success_url = '/'


class DashboardService(View):
    def get(self, request):
        mothers = BeeMother.objects.all().order_by("id")
        for mother in mothers:
            BeeMotherService.set_mother_age(mother)
            BeeMotherService.set_mother_active(mother)
        return render(request, "pages/dashboard.html", {"mothers": mothers})
