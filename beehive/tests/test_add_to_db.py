import pytest

from beehive.models import Apiary, BeeHive, BeeMother, BeeFamily
from beehive.tests.utils import (create_fake_apiary,
                                 create_fake_beehive,
                                 create_fake_mother,
                                 create_fake_beefamily)


@pytest.mark.django_db
def test_add_apiary(set_up_apiary):
    """
    Should create new apiary object and save it to database
    """
    # Given:
    apiary_before = Apiary.objects.count()

    # When:
    new_apiary = create_fake_apiary()

    # Then:
    assert Apiary.objects.count() == apiary_before + 1
    assert Apiary.objects.count() == 6


@pytest.mark.django_db
def test_add_beehive(set_up_beehive):
    """
    Should create new beehive object and save it to database
    """
    # Given:
    beehive_before = BeeHive.objects.count()

    # When:
    new_beehive = create_fake_beehive()

    # Then:
    assert BeeHive.objects.count() == beehive_before + 1
    assert BeeHive.objects.count() == 6
    assert Apiary.objects.count() == 6


@pytest.mark.django_db
def test_add_mother(set_up_mother):
    """
    Should create new mother object and save it to database
    """
    # Given:
    mother_before = BeeMother.objects.count()

    # When:
    new_mother = create_fake_mother()

    # Then:
    assert BeeMother.objects.count() == mother_before + 1
    assert BeeMother.objects.count() == 6


@pytest.mark.django_db
def test_add_family(set_up_beefamily):
    """
    Should create new family and save it to database
    """
    # Given:
    family_before = BeeFamily.objects.count()

    # When:
    new_family = create_fake_beefamily()

    # Then:
    assert BeeFamily.objects.count() == family_before + 1
    assert BeeFamily.objects.count() == 6


