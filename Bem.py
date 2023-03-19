from Student import Student

class Bem:
    # kelas untuk menampung data bem beserta method nya

    # atribut
    __student = Student()
    __role = ""
    __divisi = ""
    __programKerja = []
    __inovasi = []

    # konstruktor
    def __init__(self, s = Student()):
        self.__student = s
        self.__role = ""
        self.__divisi = ""
        self.__programKerja = []
        self.__inovasi = []

    # setter getter
    def setRole(self, role):
        self.__role = role
    def setDivisi(self, divisi):
        self.__divisi = divisi
    def addProker(self, proker):
        self.__programKerja.append(proker)
    def addInovasi(self, inovasi):
        self.__inovasi.append(inovasi)
    
    def getRoles(self):
        return self.__role
    def getDivisi(self):
        return self.__divisi
    def getProker(self):
        return self.__proker
    def getInovasi(self):
        return self.__inovasi
    
    # method
    def printProker(self):
        print("Proker nya " + self.__student.getNama())
        i = 0
        for t in self.__programKerja:
            print(str(i + 1) + ". " + t)
            i += 1

    def printInovasi(self):
        print("Inovasi nya " + self.__student.getNama())
        i = 0
        for t in self.__inovasi:
            print(str(i + 1) + ". " + t)
            i += 1

    def doProker(self):
        print("organisasi elit kuliah sulit")
    def planning(self):
        print("hmm nanti malem makan apa ya")
    def working(self):
        print("utiwi gerlong beli makan")