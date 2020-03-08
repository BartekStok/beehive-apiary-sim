from django.db import models
from beehive.constants import BEE_HIVE_TYPES


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ApiaryModel(models.Model, TimeStampMixin):
    name = models.CharField(max_length=64, verbose_name="Nazwa Pasieki")
    description = models.TextField()
    localization = models.TextField(null=True)
    area = models.FloatField(null=True)


class BeeHive(models.Model, TimeStampMixin):
    name = models.CharField(max_length=64)
    type = models.CharField(choices=BEE_HIVE_TYPES)