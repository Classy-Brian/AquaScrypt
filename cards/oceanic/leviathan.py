import card

class Leviathan(card.Card):
    id_counter = 1

    def __init__(self):
        name = "Leviathan"
        cost = 3
        power = 4
        max_hp = 4
        sigil = ["Frenzy"] # Deals double damage when low
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

        self.id = Leviathan.id_counter
        Leviathan.id_counter += 1

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"

    def desc(self):
        return f"Sigil: {self.sigil}\nDeals double damage when low"
    
    def death_mess(self):
        return f"The villain's Leviathan's relentless fury overwhelms you, its colossal form casting a shadow over your final moments."