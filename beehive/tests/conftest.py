from random import choice
import pytest
from beehive.models import BeeHive, Apiary, BeeMother, BeeFamily
from beehive.tests.utils import faker
from beehive.constants import BEE_MOTHER_TYPES, BEE_HIVE_TYPES
from .utils import *

@pytest.fixture
def set_up_mother():
    data = []
    for _ in range(5):
        mother = create_fake_mother()
        data.append(mother)
    return data

@pytest.fixture
def set_up_apiary():
    data = []
    for _ in range(5):
        apiary = create_fake_apiary()
        data.append(apiary)
    return data

@pytest.fixture
def set_up_beehive():
    data = []
    for _ in range(5):
        beehive = create_fake_beehive()
        data.append(beehive)
    return data

@pytest.fixture
def set_up_beefamily():
    data = []
    for _ in range(5):
        beefamily = create_fake_beefamily()
        data.append(beefamily)
    return data

@pytest.fixture
def set_up_all():
    set_up_apiary()
    set_up_beehive()
    set_up_mother()
    set_up_beefamily()
