import card

class MantaRay(card.Card):

    def __init__(self):
        name = "Manta Ray"
        cost = 2
        power = 1
        max_hp = 3
        sigil = "Barrier" # Blocks the next attack against it
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return f"{self.name} that costs {self.cost} with {self.max_hp}, and {self.power}. Sigil: {self.sigil}"