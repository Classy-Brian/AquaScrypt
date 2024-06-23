import card

class Dolphin(card.Card):

    def __init__(self):
        name = "Dolphin"
        cost = 2
        power = 2
        max_hp = 2
        sigil = "Echolocation" # See upcoming attack
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"

    def desc(self):
        return f"Sigil: {self.sigil}\nAllows you to see the upcoming attack."
    
    def death_mess(self):
        return f"The villain's playful Dolphin gracefully nudges you into the eternal currents with a final splash of whimsy."