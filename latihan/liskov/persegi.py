from penghitungbangundatar import PenghitungBangunDatar

class Persegi(PenghitungBangunDatar):
    
    def __init__(self, sisi: float):
        super().__init__(sisi)
    
    def hitung_luas (self):
        print(self.get_sisi()*self.get_sisi())
        
    def hitung_keliling(self):
        print(self.get_sisi()*4)