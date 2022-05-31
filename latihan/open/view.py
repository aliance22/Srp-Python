from karakter import Karakter
from karakter_pengendara import KarakterPengendara
from karakter_penembak import KarakterPenembak

class View:
    def view_nama(self, karakter: Karakter, karakter_pengendara: KarakterPengendara):
        print(karakter_pengendara.nama(karakter))
        
    def view_power(self, karakter: Karakter, karakter_pengendara: KarakterPengendara):
        print(karakter_pengendara.power(karakter))
        
    def penembak_nama(self, karakter: Karakter, karakter_penembak: KarakterPenembak):
        print(karakter_penembak.nama(karakter))
    
    def penembak_power(self, karakter: Karakter, karakter_penembak: KarakterPenembak):
        print(karakter_penembak.power(karakter))
        