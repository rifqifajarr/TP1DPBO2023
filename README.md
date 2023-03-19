# TP1DPBO2023

## Desain Program
![diagram](/Class_Diagram.png)

## Alur Program
Pada program ini, atribut seperti textbooks merupakan list yang bisa di isi beberapa data karena saya asumsikan bahwa 1 orang dapat mempunyai banyak textbooks, begitu pula dengan laptops, tugas, markers, programKerja, inovasi, dan materi. data-data tersebut dapat dimasukkan ke list dengan menggunakan method *add* sebagai pengganti *set* yang biasanya digunakan untuk set atribut. Pada kelas BEM, DPM, dan Assistant menampung Student sebagai objek agar data Student dapat diambil pada method di kelas-kelas tsb (dalam program ini contoh nya mengambil nama dari Student menggunakan getter).

## Relasi Antar Kelas
- Student dan Lecturer *extend* dari Human karena merupakan objek yang sama yaitu manusia sehingga Student dan Lecturer dapat mengambil atribut pada Human seperti nama
- BEM, DPM, dan Assistant *agregasi* dari Student. Alasan nya adalah karena anggota BEM, DPM, dan asisten praktikum merupakan mahasiswa juga sehingga kelas-kelas ini memerlukan atribut dan data dari kelas Student dan ketika objek BEM, DPM, dan Assistant nya dihapus ketika mahasiswa tersebut sudah tidak menjabat lagi, objek Student nya tetap ada tidak ikut terhapus.

# Dokumentasi
![program](/SS_Program.png)
![output](/SS_Output.png)
