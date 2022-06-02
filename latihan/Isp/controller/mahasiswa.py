from interface.tugas_mahasiswa import TugasMahasiswa

class TugasMahasiswa(TugasMahasiswa):
    def mencatat_kehadiran(self) -> None:
        print("Rekap per pertemuan")
        
    def mengerjakan_ujian(self) -> None:
        print("Mahasiswa sedang mengerjakan ujian")