from penghitungbangunruang import PenghitungBangunRuang

class Kubus(PenghitungBangunRuang):
    
    def hitung_keliling(self):
        print(12 * self.get_rusuk())
        
    def hitung_luas(self):
        print(6 * self.get_rusuk() * self.get_rusuk())
        
    def hitung_volume(self):
        print(self.get_rusuk() * self.get_rusuk() * self.get_rusuk()) 