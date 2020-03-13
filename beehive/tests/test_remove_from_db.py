import pytest

from beehive.models import Apiary, BeeHive, BeeMother, BeeFamily
from beehive.tests.utils import (create_fake_apiary,
                                 create_fake_beehive,
                                 create_fake_mother,
                                 create_fake_beefamily)


@pytest.mark.django_db
def test_remove_apiary(set_up_apiary):
    """
    Should remove apiary from database
    """
    # Given:
    apiary_before = Apiary.objects.count()

    # When:
    new_apiary = Apiary.objects.first()
    new_apiary.delete()

    # Then:
    assert Apiary.objects.count() == apiary_before - 1
    assert Apiary.objects.count() == 4


@pytest.mark.django_db
def test_remove_beehive(set_up_beehive):
    """
    Should remove beehive object from database
    """
    # Given:
    beehive_before = BeeHive.objects.count()

    # When:
    new_beehive = BeeHive.objects.first()
    new_beehive.delete()

    # Then:
    assert BeeHive.objects.count() == beehive_before - 1
    assert BeeHive.objects.count() == 4
    assert Apiary.objects.count() == 5


@pytest.mark.django_db
def test_remove_mother(set_up_mother):
    """
    Should remove mother from database
    """
    # Given:
    mother_before = BeeMother.objects.count()

    # When:
    new_mother = BeeMother.objects.first()
    new_mother.delete()

    # Then:
    assert BeeMother.objects.count() == mother_before - 1
    assert BeeMother.objects.count() == 4


@pytest.mark.django_db
def test_add_family(set_up_beefamily):
    """
    Should remove family from database
    """
    # Given:
    family_before = BeeFamily.objects.count()

    # When:
    new_family = BeeFamily.objects.first()
    new_family.delete()

    # Then:
    assert BeeFamily.objects.count() == family_before - 1
    assert BeeFamily.objects.count() == 4


