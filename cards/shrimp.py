import card
class Shrimp(card.Card):
    id_counter = 1

    def __init__(self):
        name = "Shrimp"
        cost = 0
        power = 0
        max_hp = 1
        sigil = ["None"]
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

        self.id = Shrimp.id_counter
        Shrimp.id_counter += 1

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"
    
    def desc(self):
        return f"It's a shrimp..."

    def death_mess(self):
        return f"The Shrimp's final strike may be small, but it leaves a giant mark, toppling the player with an unexpected and humbling defeat."