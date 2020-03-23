from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, Select
from django import forms
from beehive.models import Apiary, BeeHive, BeeMother, BeeFamily
from beehive.constants import BEE_HIVE_TYPES, BEE_MOTHER_TYPES


class ApiaryCreateForm(ModelForm):
    class Meta:
        model = Apiary
        fields = ['name', 'description', 'location', 'area', "user"]
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 3}),
            'location': Textarea(attrs={'cols': 50, 'rows': 3})
        }
        labels = {
            'name': 'Nazwa pasieki',
            'description': 'Opis pasieki',
            'location': 'Lokalizacja pasieki',
            'area': 'Powierzchnia',
        }


class BeeHiveCreateForm(ModelForm):
    class Meta:
        model = BeeHive
        fields = ['name', 'type', 'apiary', 'user']


class BeeMotherCreateForm(ModelForm):
    born = forms.DateInput()

    class Meta:
        model = BeeMother
        fields = ['name', 'bee_type', 'active', 'born', 'user']


class BeeFamilyCreateForm(ModelForm):
    bee_mother = forms.ModelChoiceField(
        queryset=BeeMother.objects.filter(beefamily__bee_hive__isnull=True),
        required=False
    )
    bee_hive = forms.ModelChoiceField(
        queryset=BeeHive.objects.filter(beefamily__isnull=True)
    )

    class Meta:
        model = BeeFamily
        fields = ['name', 'strength', 'bee_mother', 'bee_hive', 'user']


class AddUserForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    repeatPassword = forms.CharField(max_length=64, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeatPassword = cleaned_data.get('repeatPassword')
        login = cleaned_data.get('login')
        if password != repeatPassword:
            raise forms.ValidationError("Hasło się nie zgadza")
        try:
            user = User.objects.get(username=login)
        except User.DoesNotExist:
            return None
        if user.username == login:
            raise forms.ValidationError("Podany login już istnieje w bazie danych")


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
