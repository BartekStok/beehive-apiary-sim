import pytest
from django.test import TestCase

from beehive.tests.conftest import set_up_apiary
from beehive.tests.utils import create_fake_beehive, BeeHive, create_fake_mother


# from beehive.tests.conftest import set_up_apiary

class TestBeehive(TestCase):

    # def setUp(self) -> None:
    #     # LOAD ALL COMMON FIXTURES
    #     set_up_apiary()


    @pytest.mark.django_db
    def test_add_beehive(self):
        """
        Should create new beehive object and save it to database
        """
        # set_up_apiary()

        # Given:
        beehive_before = BeeHive.objects.count()

        # When:
        new_beehive = create_fake_beehive()

        # Then:
        assert BeeHive.objects.count() == beehive_before + 1
