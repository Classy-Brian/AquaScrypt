import card

class Shark(card.Card):

    def __init__(self):
        name = "Shark"
        cost = 1
        power = 2
        max_hp = 2
        sigil = "None"
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"

    def desc(self):
        return f"Sigil: {self.sigil}"
    
    def death_mess(self):
        return f"The villain's ferocious Shark devours you whole, leaving nothing but a lingering fear in the depths."