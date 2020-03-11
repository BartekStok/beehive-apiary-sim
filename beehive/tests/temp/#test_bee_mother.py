from random import choice

from django.test import TestCase

from beehive.constants import BEE_MOTHER_TYPES
from beehive.service.bee_mother_service import BeeMotherService
from beehive.tests.utils import create_fake_mother


# class TestBeeMother(TestCase):
#     mother_type = choice(BEE_MOTHER_TYPES)[0]
#     def test_should_create_when_valid_data(self):
#         mother = create_fake_mother()
#         assert mother.name == 'Mom'
#         assert mother.type == self.mother_type
#
#     def test_should_not_create_when_wrong_type(self):
#         pass
