from Student import Student

class Assistant:
    # kelas untuk menampung data Assistant beserta method nya

    # atribut
    __student = Student()
    __matkul = ""
    __materi = []

    # konstruktor
    def __init__(self, s = Student()):
        self.__student = s
        self.__matkul = ""
        self.__materi = []
    
    # setter and getter
    def setMatkul(self, matkul):
        self.__matkul = matkul
    def addMateri(self, materi):
        self.__materi.append(materi)
    
    def getMatkul(self):
        return self.__matkul
    def getMateri(self):
        return self.__materi
    
    # method
    def printMateri(self):
        print("Materi nya " + self.__student.getNama())
        i = 0
        for t in self.__materi:
            print(str(i + 1) + ". " + t)
            i += 1

    def ngajar(self):
        print("jadi gini adik adik..")
    
    def assignTugas(self):
        print("yah jadi tugas nya adalah..")