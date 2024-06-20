import card

class Turtle(card.Card):

    def __init__(self):
        name = "Turtle"
        cost = 1
        power = 1
        max_hp = 4
        sigil = "Shell" # Halfs damage
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return f"Sigil: {self.sigil}\nChoose a villian's card to cut the damage in half."
    
    def death_mess(self):
        return