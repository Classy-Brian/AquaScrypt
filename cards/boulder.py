import card
class Boulder(card.Card):
    id_counter = 1

    def __init__(self):
        name = "Boulder"
        cost = 0
        power = 0
        max_hp = 5
        sigil = ["None"]
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

        self.id = Boulder.id_counter
        Boulder.id_counter += 1

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"
    
    def desc(self):
        return f"It's a Boulder..."

    def death_mess(self):
        return f"The Boulder's final strike may be slow, but it leaves a crushing impact."