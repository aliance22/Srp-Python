from kartu_bank import KartuBank

class KartuKredit(KartuBank):
    
    def do_transaction(self, total : int):
        print(F"Transaksi sejumlah", total, "dilakukan dnegan menggunakan kredit")