from Human import Human

class Student (Human):
    # kelas untuk menampung data student dan method nya

    # atribut
    __nim = ""
    __textbooks = []
    __laptops = []
    __tugas = []

    # konstruktor
    def __init__(self):
        self.__nim = ""
        self.__textbooks = []
        self.__laptops = []
        self.__tugas = []
    
    # setter getter
    def setnim(self, nim):
        self.__nim = nim
    def addTextbooks(self, textbook):
        self.__textbooks.append(textbook)
    def addLaptops(self, laptop):
        self.__laptops.append(laptop)
    def addTugas(self, tugas):
        self.__tugas.append(tugas)
    
    def getNim(self):
        return self.__nim
    def getTextbooks(self):
        return self.__textbooks
    def getLaptops(self):
        return self.__laptops
    
    # method
    def printTextbooks(self):
        print("Buku Punya " + self.getNama())
        i = 0
        for t in self.__textbooks:
            print(str(i + 1) + ". " + t)
            i += 1

    def printLaptops(self):
        print("laptop Punya " + self.getNama())
        i = 0
        for t in self.__laptops:
            print(str(i + 1) + ". " + t)
            i += 1

    def printTugas(self):
        print("Tugas nya " + self.getNama())
        i = 0
        for t in self.__tugas:
            print(str(i + 1) + ". " + t)
            i += 1

    
    # prosedur untuk print data student
    def printStudent(self):
        print("")
        print("DATA " + self.getNama())
        print("Nama : " + self.getNama())
        print("Jenis Kelamin : " + self.getjenisKelamin())
        print("NIM : " + self.getNim())
        self.printTextbooks()
        self.printLaptops()
        self.printTugas()
        print("METHOD " + self.getNama())
        self.makan()
        self.minum()
        self.tidur()
        self.belajar()
        self.kuliah()
        self.nugas()

    def belajar(self):
        print("gamau belajar mau nya maen")

    def kuliah(self):
        print("skip ah ngantuk jam segitu mah :(")

    def nugas(self):
        print("ntar ajaa lah masih lama dl nya")
