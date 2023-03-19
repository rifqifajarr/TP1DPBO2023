from Student import Student

class Dpm:
    # kelas untuk menampung data dpm beserta method nya

    # atribut
    __student = Student()
    __role = ''
    __komisi = ''
    __tugas = []

    # konstruktor
    def __init__(self, s = Student()):
        self.__student = s
        self.__role = ''
        self.__komisi = ''
        self.__tugas = []
    
    # setter and getter
    def setRole(self, role):
        self.__role = role
    def setKomisi(self, komisi):
        self.__komisi = komisi
    def addTugas(self, tugas):
        self.__tugas.append(tugas)
    
    def getRole(self):
        return self.__role
    def getKomisi(self):
        return self.__komisi
    def getTugas(self):
        return self.__tugas
    
    # method
    def printTugas(self):
        print("Tugas nya " + self.__student.getNama())
        i = 0
        for t in self.__tugas:
            print(str(i + 1) + ". " + t)
            i += 1

    def ngawas(self):
        print("hmm ini panitia nya kemana ya")
    
    def apresiasi(self):
        print("yak kalian udah bagus banget")

    def rekomendasi(self):
        print("kata gw teh mending gini")
    