from balok import Balok
from balok_controller import BalokController
from balok_view import BalokView

panjang = Balok(8, 9, 10)

penghitung_balok = BalokController()
penampil_balok = BalokView()

penampil_balok.show_luas(panjang, penghitung_balok)
penampil_balok.show_keliling(panjang, penghitung_balok)
penampil_balok.show_volume(panjang, penghitung_balok)