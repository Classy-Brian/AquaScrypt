import abc 

class CardFactory(abc.ABC):

    @abc.abstractmethod
    def create_random_card(self):
        """
        Abstract method (no code) that each concrete 
        factory overrides to create and return Card objects.
        """
        pass 