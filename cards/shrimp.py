import card
class Shrimp(card.Card):

    def __init__(self):
        name = "Shrimp"
        cost = 0
        power = 0
        max_hp = 1
        sigil = "None"
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."
    
    def desc(self):
        return "It's a shrimp..."