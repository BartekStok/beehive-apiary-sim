from django.db import models
from beehive.constants import *


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Apiary(models.Model, TimeStampMixin):
    name = models.CharField(max_length=64, verbose_name="Nazwa Pasieki")
    description = models.TextField(verbose_name="Opis pasieki")
    localization = models.TextField(null=True, verbose_name="Lokalizacja")
    area = models.FloatField(null=True, verbose_name="Powierzchnia")


class BeeHive(models.Model, TimeStampMixin):
    name = models.CharField(max_length=64, verbose_name="Nazwa Ula",
                            help_text="Pozostaw puste by nadać standardową nazwę"
                            )
    type = models.CharField(choices=BEE_HIVE_TYPES, verbose_name="Typ Ula")
    apiary = models.ForeignKey(Apiary, on_delete=models.CASCADE)


class BeeMother(models.Model, TimeStampMixin):
    name = models.CharField(max_length=64, verbose_name="Nazwa Matki")
    bee_type = models.CharField(choices=BEE_MOTHER_TYPES, verbose_name="Typ pszczoły")
    age = models.DateTimeField(default="just born", verbose_name="Wiek matki")
    

