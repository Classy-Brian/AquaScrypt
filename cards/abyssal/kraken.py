import card

class Kraken(card.Card):

    def __init__(self):
        name = "Kraken"
        cost = 3
        power = 3
        max_hp = 4
        sigil = "Frenzy" # Deals double damage when low
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"

    def desc(self):
        return f"Sigil: {self.sigil}\nDeals double damage when low"
    
    def death_mess(self):
        return f"The villain's mighty Kraken ensnares you with its tentacles, dragging you into the abyss with a thunderous roar!"