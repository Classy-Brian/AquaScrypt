import card

class Otter(card.Card):

    def __init__(self):
        name = "Otter"
        cost = 1
        power = 1
        max_hp = 2
        sigil = ["Swift"] # Chance to avoid attack
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"

    def desc(self):
        return f"Sigil: {self.sigil}\n50% Chance to avoid attack."
    
    def death_mess(self):
        return f"The villain's mischievous Otter bids farewell with a cheeky slap, leaving a mark in memory of its playful antics."