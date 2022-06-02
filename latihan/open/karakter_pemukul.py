from karakter import Karakter 

class KarakterPemukul(Karakter):
    
    def nama(self, karakter : Karakter) -> str:
        return("nama", karakter.get_nama) 
    
    def power(self, karakter : Karakter) -> float:
        return("memukul", karakter.get_power)