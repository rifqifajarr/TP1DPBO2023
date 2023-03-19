#   Saya Rifqi Fajar Indrayadi dengan NIM 2101103 mengerjakan soal TP 1
#   dalam Praktikum mata kuliah Desain dan Pemrograman Berorientasi Objek, untuk keberkahan-Nya
#   maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

from Student import Student
from Lecturer import Lecturer
from Bem import Bem
from Dpm import Dpm
from Assistant import Assistant

# membuat objek rapi
rapi = Student()

# set data rapi
rapi.setNama("Rapi")
rapi.setjenisKelamin("Laki Kali")
rapi.setnim("2106789")
rapi.addTextbooks("Buku Alpro")
rapi.addTextbooks("Buku Strukdat")
rapi.addTextbooks("Buku DPBO")
rapi.addLaptops("VAIO")
rapi.addTugas("Prokon - Bikin ERD")
rapi.addTugas("Andal - WS 3")

# membuat objek kabem
kabem = Bem(rapi)
kabem.setRole("Ketua")
kabem.setDivisi("Non Divisi")
kabem.addProker("DivTalk")
kabem.addInovasi("bikin divisi baru")
kabem.addInovasi("bikin sop buat persuratan ke dosen")

# print data rapi dan kabem beserta method nya
rapi.printStudent()

print("DATA KABEM")
print("Role : " + kabem.getRoles())
print("Divisi : " + kabem.getDivisi())
kabem.printProker()
kabem.printInovasi()
print("METHOD KABEM")
kabem.doProker()
kabem.planning()
kabem.working()

# membuat objek alga
alga = Student()

# set data alga
alga.setNama("Alga")
alga.setjenisKelamin("Laki Kali")
alga.setnim("2103456")
alga.addTextbooks("Buku Basis Data")
alga.addTextbooks("Buku Kalkulus")
alga.addLaptops("Lenovo")
alga.addTugas("Andal - WS 3")
alga.addTugas("DPBO - TP 1")

# membuat objek dpm
dpm = Dpm(alga)
dpm.setRole("Staff")
dpm.setKomisi("Komisi Pengawasan")
dpm.addTugas("Mengawasi")
dpm.addTugas("Mengevaluasi")

# print data alga dan dpm beserta method nya
alga.printStudent

print("DATA DPM")
print("Role : " + dpm.getRole())
print("Komisi : " + dpm.getKomisi())
dpm.printTugas()
print("METHOD DPM")
dpm.ngawas()
dpm.apresiasi()
dpm.rekomendasi()

# membuat objek Najmi dan Bulan
najmi = Student()
bulan = Student()

# set data Najmi dan Bulan
najmi.setNama("Najmi")
najmi.setjenisKelamin("Perempuan")
najmi.setnim("2105612")
najmi.addTextbooks("Buku Kalkulus")
najmi.addTextbooks("Buku Pend Agama")
najmi.addLaptops("Lenovo Legion")
najmi.addTugas("Sistem Operasi - Bikin PPT")
najmi.addTugas("Sistem Operasi - Bikin pesaing linux")

bulan.setNama("Bulan")
bulan.setjenisKelamin("Laki Kali")
bulan.setnim("2134567")
bulan.addTextbooks("Buku Alpro")
bulan.addLaptops("HP Victus")
bulan.addTugas("PromVis - namatin modul")

# membuat objek asprak
asprak1 = Assistant()
asprak2 = Assistant()

# set data asprak
asprak1.setMatkul("Sistem Basis Data")
asprak1.addMateri("ERD")
asprak1.addMateri("Basic Query")
asprak1.addMateri("Advance Query")

asprak2.setMatkul("Alpro 2")
asprak2.addMateri("Bubble Sort")
asprak2.addMateri("Quick Sort")
asprak2.addMateri("Mesin Kata")

# print data Najmi dan Asprak1
najmi.printStudent()

print("DATA ASPRAK")
print("Matkul : " + asprak1.getMatkul())
asprak1.getMateri()
asprak1.ngajar()
asprak1.assignTugas()

bulan.printStudent()

print("DATA ASPRAK")
print("Matkul : " + asprak2.getMatkul())
asprak2.getMateri()
asprak2.ngajar()
asprak2.assignTugas()

# membuat objek bu rosa
buRosa = Lecturer()

# set data bu rosa
buRosa.setNama("Rosa")
buRosa.setjenisKelamin("Perempuan")
buRosa.setNip("1234567890")
buRosa.addMarker("Snowman Hitam")
buRosa.addMarker("Snowman Biru")
buRosa.addLaptops("Lenovo Thinkpad")
buRosa.addLaptops("Acer Aspire")

# print data bu rosa
print("")
print("DATA DOSEN")
print("Nama : " + buRosa.getNama())
print("Jenis Kelamin : " + buRosa.getjenisKelamin())
print("NIP : " + buRosa.getNip())
buRosa.printMarkers()
buRosa.printLaptops()
print("METHOD DOSEN")
buRosa.ngajar()
buRosa.assignTugas()
buRosa.giveScore()

# membuat objek afri
afri = Student()

# set data afri
afri.setNama("Afri")
afri.setjenisKelamin("Laki Kali")
afri.setnim("2119876")
afri.addTextbooks("Buku PPKN")
afri.addTextbooks("Buku Pend Agama")
afri.addTextbooks("Buku B Indonesia")
afri.addLaptops("Acer Aspire")
afri.addTugas("Andal - WS 3")
afri.addTugas("MetLit - nyari jurnal")

# print data afri
afri.printStudent()

# membuat objek anin
anin = Student()

# set data anin
anin.setNama("Anin")
anin.setjenisKelamin("Perempuan")
anin.setnim("2125467")
anin.addTextbooks("Buku Kalkulus")
anin.addTextbooks("Buku Aljabar")
anin.addLaptops("Lenovo Yoga")
anin.addLaptops("Asus Vivobook Duo")
anin.addTugas("DPBO - TP1")
anin.addTugas("PromVis - namatin modul")
anin.addTugas("MetLit - nyari jurnal")

# print data anin
anin.printStudent()