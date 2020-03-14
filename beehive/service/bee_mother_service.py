import math

from django.utils import timezone

from beehive.models import BeeMother


class BeeMotherService():

    """Creates Bee Mother"""
    @staticmethod
    def create(name, bee_type):
        return BeeMother.objects.create(name, bee_type)

    """Checks if mother age is less than 1825 days (5 years)"""
    @staticmethod
    def set_mother_active(mother):
        if math.fabs(mother.age.days) > 1825:
            mother.active = False
            mother.save()
        return mother

    """Sets mother age"""
    @staticmethod
    def set_mother_age(mother):
        age = mother.born - timezone.now()
        parse_age = int(math.fabs(age.days))
        mother.age = age
        mother.save()
        return parse_age

