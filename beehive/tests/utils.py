from faker import Faker
from beehive.models import *
from random import randint, choice

faker = Faker("pl_PL")

def create_fake_apiary():
    """Generate new apiary and saves to database"""
    new_apiary = Apiary.objects.create(
            name=faker.word(),
            description=faker.sentence(),
            location=faker.address(),
            area=randint(1, 10)
        )
    return new_apiary

def create_fake_mother():
    """Generate new mother and saves to database"""
    new_mother = BeeMother.objects.create(
            name=faker.word(),
            bee_type=choice(BEE_MOTHER_TYPES)[0],
        )
    return new_mother

def create_fake_beehive():
    """Generate new beehive and saves to database"""
    apiary = Apiary.objects.first()
    new_beehive = BeeHive.objects.create(
        name=faker.word(),
        type=choice(BEE_HIVE_TYPES)[0],
        apiary=apiary
    )
    return new_beehive

def create_fake_beefamily():
    """Generate new beefamily and saves to database"""
    bee_hive = BeeHive.objects.filter(
        beefamily__isnull=True
    )
    bee_mother = BeeMother.objects.filter(
        beefamily__bee_hive__isnull=True
    )
    new_beefamily = BeeFamily.objects.create(
        name=faker.word(),
        strength=randint(5000, 50000),
        bee_mother=bee_mother,
        bee_hive=bee_hive
    )
    return new_beefamily