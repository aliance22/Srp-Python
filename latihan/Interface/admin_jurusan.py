from interface.tugas_adminJurusan import TugasAdminJurusan

class AdminJurusan (TugasAdminJurusan) :
    
    def mencatat_kehadiran(self) -> None :
        print("Rekap per semester dari semua dosen")
        
    def pubilkasi_jadwal(self) -> None :
        prnt ("Admin jurusan mempubikasi jadwal ujian")