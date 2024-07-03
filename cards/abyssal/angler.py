import card

class Angler(card.Card):
    id_counter = 1

    def __init__(self):
        name = "Angler"
        cost = 1
        power = 2
        max_hp = 1
        sigil = ["Bioluminescence"] # Other abyssal fish gets 1+ stat
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

        self.id = Angler.id_counter
        Angler.id_counter += 1

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"

    def desc(self):
        return f"Sigil: {self.sigil}\nEnhances itself and other abyssal fish cards, giving them +1 to their stats."
    
    def death_mess(self):
        return f"The villain's Angler deceived you and has reeled you in! Better luck next time, suckerfish!"