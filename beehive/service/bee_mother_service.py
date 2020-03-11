from beehive.models import BeeMother


class BeeMotherService():

    @staticmethod
    def create(name, bee_type):
        return BeeMother.objects.create(name, bee_type)
