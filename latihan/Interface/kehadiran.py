from abc import ABC , abstractmethod

class Kehadiran(ABC):
    
    @abstractmethod
    def mencatat_kahadiran(self) -> None:
        pass