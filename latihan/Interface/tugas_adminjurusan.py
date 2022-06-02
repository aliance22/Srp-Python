from interface.kehadiran_operation import KehadiranOperation
from abc import ABC, abstractmethod

class TugasAdminJurusan(KehadiranOperation, ABC):
    @abstractmethod
    def mencatat_kehadiran(self) -> None:
        super().mencatat_kehadiran()
        
    @abstractmethod
    def membuat_ujian(self) -> None:
        pass