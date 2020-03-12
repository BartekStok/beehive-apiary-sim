from django.core.management import BaseCommand
from random import randint, choice
from faker import Faker
import pytz
from beehive.models import *


class Command(BaseCommand):
    help = 'Tekst pomocy'

    def handle(self, *args, **options):
        faker = Faker("pl_PL")
        for i in range(1, 10):
            beehive = BeeHive()
            beehive.name = f"Hive {i} - {faker.word()}"
            beehive.type = choice(BEE_HIVE_TYPES)[0]
            apiary = choice(Apiary.objects.all())
            beehive.apiary = apiary
            beehive.save()
