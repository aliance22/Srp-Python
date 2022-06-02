from tugas.dosen import Dosen
from tugas.mahasiswa import Mahasiswa
from tugas.admin_jurusan import AdminJurusan

mahasiswa = Mahasiswa()
admin_jurusan = AdminJurusan()
dosen = Dosen()
mahasiswa.mencatat_kehadiran()
dosen.mencatat_kehadiran()
admin_jurusan.mencatat_kehadiran()

admin_jurusan.mempublis_jadwal()
dosen.membuat_ujian()
mahasiswa.mengerjakan_ujian()