import card

class Turtle(card.Card):

    def __init__(self):
        name = "Turtle"
        cost = 1
        power = 1
        max_hp = 4
        sigil = ["Shell"] # Halfs damage
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"

    def desc(self):
        return f"Sigil: {self.sigil}\nChoose a villian's card to cut the damage in half."
    
    def death_mess(self):
        return f"The villain's ancient Turtle withdraws into its shell, leaving a lasting legacy of resilience and wisdom."