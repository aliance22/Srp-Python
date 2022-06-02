from interface.kehadiran_operation import KehadiranOperation
from abc import ABC, abstractmethod

class MahasiswaOperation(KehadiranOperation, ABC):
    
    @abstractmethod
    def mencatat_kehadiran(self) -> None:
        super().mencatat_kehadiran()
        
    @abstractmethod
    def mengerjakan_ujian(self) -> None:
        pass