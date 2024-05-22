import card

class Angler(card.Card):

    def __init__(self):
        name = "Angler"
        cost = 1
        power = 2
        max_hp = 1
        sigil = "Bioluminescence" # Other abyssal fish gets 1+ stat
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return f"{self.name} that costs {self.cost} with {self.max_hp}, and {self.power}. Sigil: {self.sigil}"