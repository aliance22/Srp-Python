from abc import ABC, abstractmethod

class PenghitungBangunRuang(ABC):
    
    def __init__(self, rusuk: float):
        self.rusuk = rusuk
   
    def get_rusuk(self, rusuk: float):
        self.rusuk = rusuk
    
    @abstractmethod
    def hitung_luas():
        pass
    
    @abstractmethod
    def hitung_keliling():
        pass
    
    @abstractmethod
    def hitung_volume():
        pass