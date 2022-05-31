from abc import ABC, abstractmethod

class Karakter(ABC):
    
    def __init__(self, nama : str, power : int):
        self.nama = nama
        self.power = power
        
    def set_nama(self, nama :str):
        self.nama = nama
        
    def get_nama(self) -> float:
        return self.nama
    
    def set_power(self, power : int):
        self.power = power
        
    def get_power(self) -> float:
        return self.power