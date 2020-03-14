from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from beehive.forms import (ApiaryCreateForm,
                           BeeHiveCreateForm,
                           BeeFamilyCreateForm,
                           BeeMotherCreateForm, LoginForm, AddUserForm)
from beehive.models import *
from beehive.service.bee_hive_service import BeeHiveService
from beehive.service.bee_mother_service import *


class IndexView(View):
    def get(self, request):
        # user = User.objects.first()
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
        beemother = BeeMother.objects.all().order_by("id")
        for mother in beemother:
            BeeMotherService.set_mother_age(mother)
            BeeMotherService.set_mother_active(mother)
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
    def get(self, request, pk):
        BeeHiveService.set_beehive_service_date(pk)
        return redirect(f'/beehive_view/{pk}')


class BeeHiveTakeHoney(View):
    def get(self, request, pk):
        BeeHiveService.set_honey_taken_date(pk)
        return redirect(f'/beehive_view/{pk}')


class BeeFamilyCreateView(CreateView):
    template_name = 'forms/beefamily_create_form.html'
    form_class = BeeFamilyCreateForm
    success_url = '/'


class BeeFamilyUpdateView(UpdateView):
    model = BeeFamily
    form_class = BeeFamilyCreateForm
    template_name = "forms/beefamily_update_form.html"
    success_url = reverse_lazy("beefamily-list-view")


class BeeFamilyDeleteView(DeleteView):
    model = BeeFamily
    template_name = "forms/beefamily_delete_form.html"
    success_url = reverse_lazy("beefamily-list-view")


class BeeMotherCreateView(CreateView):
    template_name = 'forms/beemother_create_form.html'
    form_class = BeeMotherCreateForm
    success_url = '/'


class BeeMotherUpdateView(UpdateView):
    model = BeeMother
    form_class = BeeMotherCreateForm
    template_name = "forms/beemother_create_form.html"
    success_url = reverse_lazy("beemother-list-view")


class BeeMotherDeleteView(DeleteView):
    model = BeeMother
    template_name = "forms/beemother_delete_form.html"
    success_url = reverse_lazy("beemother-list-view")


class DashboardService(View):
    def get(self, request):
        mothers = BeeMother.objects.all().order_by("id")
        for mother in mothers:
            BeeMotherService.set_mother_age(mother)
            BeeMotherService.set_mother_active(mother)
        return render(request, "pages/dashboard.html", {"mothers": mothers})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "forms/login_form.html", {"form": form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return HttpResponse("Błąd logowania")


class LogutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, "forms/add_user_form.html", {"form": form})
    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=login, email=email, password=password, first_name=first_name, last_name=last_name)
            return redirect("/")
        else:
            return render(request, "forms/add_user_form.html", {"form": form})

