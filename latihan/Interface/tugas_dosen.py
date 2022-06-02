from interface.kehadiran_operation import KehadiranOperation
from abc import ABC, abstractmethod

class TugasDosen(KehadiranOperation, ABC):
    @abstractmethod
    def mencatat_kehadiran(self) -> None:
        super().mencatat_kehadiran()
        
    def membuat_ujian(self) -> None:
        pass