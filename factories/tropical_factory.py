import random
from factories import card_factory
from cards.tropical import otter, dolphin, turtle

class TropicalFactory(card_factory.CardFactory):

    def create_random_card(self):
        tropical_enemies = random.randint(1,3)

        if tropical_enemies == 1:
            return otter.Otter()
        elif tropical_enemies == 2:
            return dolphin.Dolhpin()
        elif tropical_enemies == 3:
            return turtle.Turtle()