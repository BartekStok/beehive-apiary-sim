from django.core.management import BaseCommand
from random import randint, choice
from faker import Faker
from datetime import datetime
import pytz
from beehive.models import *
from beehive.constants import BEE_MOTHER_TYPES


class Command(BaseCommand):
    help = 'Tekst pomocy'

    def handle(self, *args, **options):
        faker = Faker("pl_PL")
        for i in range(1, 10):
            beemother = BeeMother()
            beemother.name = f"Queen {i} - {faker.name()}"
            beemother.bee_type = choice(BEE_MOTHER_TYPES)[0]
            timezone = pytz.timezone("America/Los_Angeles")
            fakeDate = faker.past_datetime(start_date='-2500d', tzinfo=timezone)
            beemother.born = fakeDate
            beemother.save()
