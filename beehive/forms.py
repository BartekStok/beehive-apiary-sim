from django.forms import ModelForm, Textarea, Select
from beehive.models import Apiary, BeeHive, BeeMother, BeeFamily
from beehive.constants import BEE_HIVE_TYPES, BEE_MOTHER_TYPES

class ApiaryCreateForm(ModelForm):
    class Meta:
        model = Apiary
        fields = ['name', 'description', 'location', 'area']
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
        fields = ['name', 'type', 'apiary']
        # widgets = {
        #     'type': Select(choices=BEE_HIVE_TYPES)
        # }

class BeeMotherCreateForm(ModelForm):
    class Meta:
        model = BeeMother
        fields = ['name', 'bee_type', 'age', 'active']
        # widgets = {
        #     'bee_type': Select(choices=BEE_MOTHER_TYPES)
        # }

class BeeFamilyCreateForm(ModelForm):
    class Meta:
        model = BeeFamily
        fields = ['name', 'strength', 'bee_mother', 'bee_hive']
