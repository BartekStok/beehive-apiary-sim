from beehive.models import *


class BeeHiveService():
    """Sets service date for BeeHive"""

    @staticmethod
    def set_beehive_service_date(beehive_id):
        beehive = BeeHive.objects.get(id=beehive_id)
        beehive.service_date = timezone.now()
        beehive.save()
        return beehive

    """Sets honey taken date"""

    @staticmethod
    def set_honey_taken_date(beehive_id):
        beehive = BeeHive.objects.get(id=beehive_id)
        beehive.honey_taken_date = timezone.now()
        beehive.save()
        return beehive
