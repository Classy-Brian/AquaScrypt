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
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return f"Sigil: {self.sigil}\nDeals double damage when low"
    
    def death_mess(self):
        return