import pytest
from .utils import *
from .conftest import *


@pytest.mark.django_db
def test_add_apiary(set_up_apiary):
    """
    Should return apiary object
    """
    # Given:
    apiary_before = Apiary.objects.count()

    # When:
    new_apiary = create_fake_apiary()

    # Then:
    assert Apiary.objects.count() == apiary_before + 1

