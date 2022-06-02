from abc import ABC, abstractmethod

class PenghitungBangunDatar(ABC):
    
    def __init__(self, sisi: float):
        self.sisi = sisi
    
    @abstractmethod
    def hitung_luas():
        pass
    
    @abstractmethod
    def hitung_keliling():
        pass