import card

class MantaRay(card.Card):
    id_counter = 1

    def __init__(self):
        name = "Manta Ray"
        cost = 2
        power = 1
        max_hp = 3
        sigil = ["Barrier"] # Blocks the next attack against it
        barrier = False
        super().__init__(name, cost, power, max_hp, sigil, barrier)

        self.id = MantaRay.id_counter
        MantaRay.id_counter += 1

    def attack(self, entity):
        entity.take_damage(self._power)
        return f"Your {self._name} delt {str(self._power)} damage to villian {entity._name}"

    def desc(self):
        return f"Sigil: {self.sigil}\nBlocks the next attack against the card that has this sigil."
    
    def death_mess(self):
        return f"The villain's graceful Manta Ray glides past, leaving you to ponder its beauty as your vision fades into darkness."