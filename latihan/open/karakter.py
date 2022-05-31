class Karakter:
    
    def __init__(self, nama : str, power : int):
        self.nama = nama
        self.power = power
        
    def menyerang(self) -> str:
        print("80 damage")
