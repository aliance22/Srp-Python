from abc import ABC , abstractmethod

class KehadiranOperation(ABC):
    
    @abstractmethod
    def mencatat_kahadiran(self) -> None:
        pass