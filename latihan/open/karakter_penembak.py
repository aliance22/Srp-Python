from karakter import Karakter

class KarakterPenembak(Karakter):
    
    def __init__(self, nama: str, power: int):
        super().__init__(nama,power)
        
    def menyerang(self):
        return self.get_power()