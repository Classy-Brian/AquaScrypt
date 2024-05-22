import random
from factories import card_factory
from cards.abyssal import angler, jellyfish, kraken

class abyssalFactory(card_factory.CardFactory):

    def create_random_card(self):
        abyssal_enemies = random.randint(1,3)

        if abyssal_enemies == 1:
            return angler.Angler()
        elif abyssal_enemies == 2:
            return jellyfish.Jellyfish()
        elif abyssal_enemies == 3:
            return kraken.Kraken()