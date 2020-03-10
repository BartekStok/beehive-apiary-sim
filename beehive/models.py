from django import forms
from django.db import models
from beehive.constants import BEE_HIVE_TYPES, BEE_MOTHER_TYPES


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Apiary(TimeStampMixin):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.TextField(null=True)
    area = models.FloatField(null=True)

    def __str__(self):
        return self.name

class BeeHive(TimeStampMixin):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64, choices=BEE_HIVE_TYPES)
    apiary = models.ForeignKey(Apiary, on_delete=models.CASCADE)
    service_date = models.DateTimeField(null=True)
    honey_taken_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.name} -- {self.type}'

class BeeMother(TimeStampMixin):
    name = models.CharField(max_length=64)
    bee_type = models.CharField(max_length=64, choices=BEE_MOTHER_TYPES)
    age = models.DurationField(default=0, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class BeeFamily(TimeStampMixin):
    name = models.CharField(max_length=64)
    strength = models.IntegerField(null=True)
    bee_mother = models.OneToOneField(BeeMother, on_delete=models.CASCADE, null=True)
    bee_hive = models.OneToOneField(BeeHive, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
