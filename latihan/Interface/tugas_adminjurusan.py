from interface.kehadiran import Kehadiran
from abc import ABC, abstractmethod

class TugasAdminJurusan(Kehadiran, ABC):
    @abstractmethod
    def mencatat_kehadiran(self) -> None:
        super().mencatat_kehadiran()
        
    @abstractmethod
    def membuat_ujian(self) -> None:
        pass