from kehadiran_operation import KehadiranOperation
from mahasiswa_operation import MahasiswaOperation
from dosen_operation import DosenOperation
from admin_operation import AdminOperation

mahasiswa1 = MahasiswaOperation()
mahasiswa2 = MahasiswaOperation()
dosen1 = DosenOperation()
dosen2 = DosenOperation()
admin1 = AdminOperation()
admin2 = AdminOperation()

mahasiswa1.mencatat_kehadiran()
mahasiswa2.mengerjakan_ujian()
dosen1.mencatat_kehadiran()
dosen2.membuat_ujian()
admin1.mencatat_kehadiran()
admin2.mempublis_jadwal_ujian()