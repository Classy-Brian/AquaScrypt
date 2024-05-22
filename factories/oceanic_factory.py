import random
from factories import card_factory
from cards.oceanic import leviathan, manta_ray, shark

class OceanicFactory(card_factory.CardFactory):

    def create_random_card(self):
        oceanic_enemies = random.randint(1,3)

        if oceanic_enemies == 1:
            return leviathan.Leviathan()
        elif oceanic_enemies == 2:
            return manta_ray.MantaRay()
        elif oceanic_enemies == 3:
            return shark.Shark()