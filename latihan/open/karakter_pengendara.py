from karakter import Karakter 

class KarakterPengendara(Karakter):
    
    def nama(self, karakter : Karakter) -> str:
        return("nama", karakter.get_nama) 
    
    def power(self, karakter : Karakter) -> float:
        return("gas", karakter.get_power)