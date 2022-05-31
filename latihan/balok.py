class Balok:
    
    def __init__(self, panjang: float, lebar: float, tinggi: float):
        self.__panjang = panjang
        self.__lebar = lebar
        self.__tinggi = tinggi 
        
    def set_panjang(self, panjang: float):
        self.__panjang(panjang)
        
    def get_panjang(self) -> float:
        return self.__panjang
    
    def set_lebar(self, lebar: float):
        self.__lebar(lebar)
        
    def get_lebar(self) -> float:
        return self.__lebar
    
    def set_tinggi(self, tinggi: float):
        self.__tinggi(tinggi)
        
    def get_tinggi(self) -> float:
        return self.__tinggi