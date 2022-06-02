from abc import ABC, abstractmethod

class Karakter(ABC):
    
    def __init__(self, nama : str, power : int):
        self.__nama = nama
        self.__power = power
    
    def get_nama(self) -> float:
        return self.__nama
    
    def get_power(self) -> float:
        return self.__power
    
    abstractmethod
    def menyerang(type : str) -> str :
        pass