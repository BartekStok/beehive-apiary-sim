from django.contrib.auth.models import User
from django.db.models import Q
from django.forms import ModelForm, Textarea, Select, Form
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


class BeeHiveCreateForm(ModelForm, Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(BeeHiveCreateForm, self).__init__(*args, **kwargs)
        self.fields['apiary'].queryset = Apiary.objects.filter(user_id=self.user.id)
    class Meta:
        model = BeeHive
        fields = ['name', 'type', 'apiary', 'user']


class BeeMotherCreateForm(ModelForm):
    born = forms.DateInput()

    class Meta:
        model = BeeMother
        fields = ['name', 'bee_type', 'active', 'born', 'user']


class BeeFamilyCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(BeeFamilyCreateForm, self).__init__(*args, **kwargs)
        self.fields['bee_mother'].queryset = BeeMother.objects.filter(
            Q(user_id=self.user.id) & Q(beefamily__bee_hive__isnull=True)
        )
        self.fields['bee_hive'].queryset = BeeHive.objects.filter(
            Q(user_id=self.user.id) & Q(beefamily__isnull=True)
        )
    class Meta:
        model = BeeFamily
        fields = ['name', 'strength', 'bee_mother', 'bee_hive', 'user']


class BeeFamilyUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(BeeFamilyUpdateForm, self).__init__(*args, **kwargs)
        self.fields['bee_mother'].queryset = BeeMother.objects.filter(
            user_id=self.user.id
        )
        self.fields['bee_hive'].queryset = BeeHive.objects.filter(
            user_id=self.user.id
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
