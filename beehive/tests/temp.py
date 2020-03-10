from random import choices, choice

from beehive.models import BeeHive
from beehive.tests.utils import faker
from beehive.constants import BEE_MOTHER_TYPES


print(choice(BEE_MOTHER_TYPES)[0])
