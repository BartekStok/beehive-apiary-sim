from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from beehive.forms import (ApiaryCreateForm,
                           BeeHiveCreateForm,
                           BeeFamilyCreateForm,
                           BeeMotherCreateForm)


class IndexView(View):
    def get(self, request):
        return render(request, "pages/index.html")


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

