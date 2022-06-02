from abc import ABC, abstractmethod

class KartuBank(ABC):
    
    @abstractmethod
    def do_transaction(self, total : int):
        pass