from django.core.management import BaseCommand
from random import randint, choice
from faker import Faker
from beehive.models import *


class Command(BaseCommand):
    help = 'Tekst pomocy'

    def handle(self, *args, **options):
        faker = Faker("pl_PL")
        for i in range(1, 10):
            beefamily = BeeFamily()
            beefamily.name = f"Family {i} - {faker.word()}"
            beefamily.strength = randint(10, 80000)
            bee_mother = choice(BeeMother.objects.filter(
                beefamily__bee_hive__isnull=True
            ))
            bee_hive = choice(BeeHive.objects.filter(
                beefamily__bee_mother__isnull=True
            ))
            beefamily.bee_mother = bee_mother
            beefamily.bee_hive = bee_hive
            beefamily.save()
