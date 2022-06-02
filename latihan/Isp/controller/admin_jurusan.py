from interface.tugas_adminjurusan import TugasAdminJurusan

class AdminJurusan (TugasAdminJurusan):
    
    def mencatat_kehadiran(self) -> None :
        print("Rekap per semester dari semua dosen")
        
    def mempublis_jadwal(self) -> None :
        print ("Admin jurusan mempubikasi jadwal ujian")