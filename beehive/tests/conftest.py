import pytest
from beehive.models import BeeHive
from .utils import faker

@pytest.fixture
def set_up_queen():
    data = []
    for _ in range(5):
        queen = BeeHive.objects.create(name=faker.word())
        data.append(queen)
    return data

@pytest.fixture
def set_up_all():
   beeHives =  set_up_queen()