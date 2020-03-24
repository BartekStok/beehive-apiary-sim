from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from beehive.forms import (ApiaryCreateForm,
                           BeeHiveCreateForm,
                           BeeFamilyCreateForm,
                           BeeMotherCreateForm, LoginForm, AddUserForm)
from beehive.models import Apiary, BeeHive, BeeMother, BeeFamily
from beehive.service.bee_hive_service import BeeHiveService
from beehive.service.bee_mother_service import BeeMotherService


class IndexView(View):
    def get(self, request):
        return render(request, "pages/index.html")


class ApiaryListView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        apiary = Apiary.objects.filter(user_id=user.id).order_by("id")
        return render(request, "pages/apiary_list_view.html", {"apiary": apiary})


class ApiaryView(LoginRequiredMixin, View):
    def get(self, request, apiary_id):
        apiary = Apiary.objects.get(id=apiary_id)
        return render(request, "pages/apiary_view.html", {"apiary": apiary})


class BeeHiveListView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        beehive = BeeHive.objects.filter(user_id=user.id).order_by("id")
        return render(request, "pages/beehive_list_view.html", {"beehive": beehive})


class BeeHiveView(LoginRequiredMixin, View):
    def get(self, request, beehive_id):
        beehive = BeeHive.objects.get(id=beehive_id)
        return render(request, "pages/beehive_view.html", {"beehive": beehive})


class BeeFamilyListView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        beefamily = BeeFamily.objects.filter(user_id=user.id).order_by("id")
        return render(request, "pages/beefamily_list_view.html", {"beefamily": beefamily})


class BeeFamilyView(LoginRequiredMixin, View):
    def get(self, request, beefamily_id):
        beefamily = BeeFamily.objects.get(id=beefamily_id)
        return render(request, "pages/beefamily_view.html", {"beefamily": beefamily})


class BeeMotherListView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        beemother = BeeMother.objects.filter(user_id=user.id).order_by("id")
        for mother in beemother:
            BeeMotherService.set_mother_age(mother)
            BeeMotherService.set_mother_active(mother)
        return render(request, "pages/beemother_list_view.html", {"beemother": beemother})


class BeeMotherView(LoginRequiredMixin, View):
    def get(self, request, beemother_id):
        beemother = BeeMother.objects.get(id=beemother_id)
        return render(request, "pages/beemother_view.html", {"beemother": beemother})


class ApiaryCreateView(LoginRequiredMixin, FormView):
    def get(self, request):
        form = ApiaryCreateForm(initial={'user': request.user})
        return render(request, "forms/apiary_create_form.html", {"form": form})
    def post(self, request):
        form = ApiaryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apiary-list-view')
        else:
            return render(request, "forms/apiary_create_form.html", {"form": form})


class ApiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Apiary
    form_class = ApiaryCreateForm
    template_name = "forms/apiary_update_form.html"
    success_url = reverse_lazy("apiary-list-view")


class ApiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Apiary
    template_name = "forms/apiary_delete_form.html"
    success_url = reverse_lazy("apiary-list-view")


class BeeHiveCreateView(LoginRequiredMixin, FormView):
    def get(self, request):
        form = BeeHiveCreateForm(initial={"user": request.user})
        form.fields['apiary'].queryset = Apiary.objects.filter(user_id=request.user)
        return render(request, 'forms/beehive_create_form.html', {"form": form})
    def post(self, request):
        form = BeeHiveCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beehive-list-view')
        else:
            return HttpResponse("Błąd formularza")


class BeeHiveUpdateView(LoginRequiredMixin, UpdateView):
    model = BeeHive
    form_class = BeeHiveCreateForm
    template_name = "forms/beehive_update_form.html"
    success_url = reverse_lazy("beehive-list-view")


class BeeHiveDeleteView(LoginRequiredMixin, DeleteView):
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


class BeeFamilyCreateView(LoginRequiredMixin, FormView):
    def get(self, request, *args, **kwargs):
        form = BeeFamilyCreateForm(initial={"user": request.user})
        form.fields['bee_mother'].queryset = BeeMother.objects.filter(user_id=request.user)
        form.fields['bee_hive'].queryset = BeeHive.objects.filter(user_id=request.user)
        return render(request, "forms/beefamily_create_form.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = BeeFamilyCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beefamily-list-view')
        else:
            return render(request, "forms/beefamily_create_form.html", {"form": form})



class BeeFamilyUpdateView(LoginRequiredMixin, UpdateView):
    model = BeeFamily
    form_class = BeeFamilyCreateForm
    template_name = "forms/beefamily_update_form.html"
    success_url = reverse_lazy("beefamily-list-view")


class BeeFamilyDeleteView(LoginRequiredMixin, DeleteView):
    model = BeeFamily
    template_name = "forms/beefamily_delete_form.html"
    success_url = reverse_lazy("beefamily-list-view")


class BeeMotherCreateView(LoginRequiredMixin, FormView):
    def get(self, request, *args, **kwargs):
        form = BeeMotherCreateForm(initial={"user": request.user})
        return render(request, "forms/beemother_create_form.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = BeeMotherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beemother-list-view')
        else:
            return render(request, "forms/beemother_create_form.html", {"form": form})


class BeeMotherUpdateView(LoginRequiredMixin, UpdateView):
    model = BeeMother
    form_class = BeeMotherCreateForm
    template_name = "forms/beemother_create_form.html"
    success_url = reverse_lazy("beemother-list-view")


class BeeMotherDeleteView(LoginRequiredMixin, DeleteView):
    model = BeeMother
    template_name = "forms/beemother_delete_form.html"
    success_url = reverse_lazy("beemother-list-view")


class DashboardService(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        mothers = BeeMother.objects.filter(user_id=user.id).order_by("id")
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
            login_user = form.cleaned_data['login']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username=login_user,
                                     email=email,
                                     password=password,
                                     first_name=first_name,
                                     last_name=last_name)
            return redirect("/")
        else:
            return render(request, "forms/add_user_form.html", {"form": form})
