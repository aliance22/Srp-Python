from kartu_bank import KartuBank
from kartu_debit import KartuDebit
from kartu_kredit import KartuKredit
from transaksi import Transaksi

debit = KartuDebit()
kredit = KartuKredit()

transaksi = Transaksi(debit)
transaksi.do_paymen(100000)

transaksi2 = Transaksi(kredit)
transaksi2.do_paymen(500000)
