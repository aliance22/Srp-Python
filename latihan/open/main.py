from karakter_pemukul import KarakterPemukul
from karakter_pengendara import KarakterPengendara
from karakter_penembak import KarakterPenembak

karakter1 = KarakterPemukul ("waladolin",80)
print(karakter1.menyerang(),"memukul")

karakter2 = KarakterPenembak ("amin",90)
print(karakter2.menyerang(),"memukul")

karakter3 = KarakterPengendara ("stepen",69)
print(karakter3.menyerang(),"run")