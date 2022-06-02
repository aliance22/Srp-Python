from kartu_bank import KartuBank

class KartuDebit(KartuBank):
    
    def do_transaction(self, total : int):
        print(F"Transaksi sebesar {total} dilakukan dengan menggunakan debit")