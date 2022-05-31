from karakter import Karakter

class KarakterPenembak(Karakter):
    
    def nama(self, karakter: Karakter) -> str:
        return("nama", karakter.get_nama)
        
    def power(self, karakter: Karakter) -> float:
        return("menembak", karakter.get_power)