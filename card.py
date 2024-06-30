import abc

class Card(abc.ABC):
    """ Represents a single card
    Attributes:
        <<get>> _name (string): Name of the card
        <<get>> _hp (int): health of the card
        _max_hp (int): max health of the card
        _cost (int): cost of the card
        <<get>> _power (int): power of the card
        _sigil (string): sigil of the card
    """

    def __init__(self, name, cost, power, max_hp, sigil, barrier):
        """ Initializes attributes """
        self._name = name
        self._cost = cost
        self._power = power
        self._max_hp = max_hp
        self._hp = max_hp
        self._sigil = sigil
        self.barrier = barrier
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            cost=data.get('cost'),
            power=data.get('power'),
            max_hp=data.get('max_hp'),
            sigil=data.get('sigil'),
            barrier=data.get('barrier')
        )

    @property
    def name(self):
        """ Getter for name """
        return self._name

    @property
    def max_hp(self):
        return self._max_hp
    
    @name.setter
    def name(self, newName):
        self._name = newName
    
    @max_hp.setter
    def max_hp(self, value):
        self._max_hp = value

    @property
    def hp(self):
        """ Getter for health """
        return self._hp
    
    @hp.setter
    def hp(self, value):
        """ Setter for health """
        self._hp = value

    @property
    def power(self):
        """ Getter for power """
        return self._power
    
    @power.setter
    def power(self, value):
        """ Setter for health """
        self._power = value

    @property
    def cost(self):
        """ Getter for cost """
        return self._cost

    @cost.setter
    def cost(self, value):
        """ Setter for health """
        self._cost = value

    @property
    def sigil(self):
        """ Getter for sigil """
        return self._sigil

    @sigil.setter
    def sigil(self, value):
        """ Setter for health """
        self._sigil = value

    def take_damage(self, dmg):
        """ Takes damge, subtracts health from damage """
        if self._hp > dmg:
            self._hp -= dmg
        else:
            self._hp = 0
        return f"{self.name} takes {dmg} damage"

    @abc.abstractmethod
    def attack(self, entity):
        """ Deals damage to opposing entity """
        pass

    @abc.abstractmethod
    def desc(self):
        """ Description of the sigil """
        pass

    @abc.abstractmethod
    def death_mess(self):
        """ Card message when killing you """
        pass

    def __str__(self):
        """ returns name, health, and sigil """
        return f"{self.name} \n Cost: {self.cost} \n HP:{self._hp}/{self._max_hp} \n Power: {self.power} \n Sigil: {self._sigil}"

class AttackCard(Card):
    def __init__(self, name, cost, power, max_hp, sigil, barrier, attack_message, death_message, description):
        super().__init__(name, cost, power, max_hp, sigil, barrier)
        self.attack_message = attack_message
        self.death_message = death_message
        self.description = description

    def attack(self):
        # Implementation of attack method
        pass

    def death_mess(self):
        # Implementation of death_mess method
        pass

    def desc(self):
        # Implementation of desc method
        pass

    @staticmethod
    def from_dict(data):
        return AttackCard(
            name=data.get('name'),
            cost=data.get('cost'),
            power=data.get('power'),
            max_hp=data.get('max_hp'),
            sigil=data.get('sigil'),
            barrier=data.get('barrier'),
            attack_message=data.get('attack_message'),
            death_message=data.get('death_message'),
            description=data.get('description')
        )