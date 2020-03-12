import os
import sys
import pytest
from beehive.tests.utils import faker, create_fake_mother, create_fake_apiary, create_fake_beehive, \
    create_fake_beefamily

sys.path.append(os.path.dirname(__file__))


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
    pass
