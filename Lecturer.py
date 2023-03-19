from Human import Human

class Lecturer (Human):
    # kelas untuk menampung data lecturer dan method nya

    # atribut
    __nip = ""
    __markers = []
    __laptops = []

    # konstruktor
    def __init__(self):
        self.__nip = ""
        self.__markers = []
        self.__laptops = []
    
    # setter getter
    def setNip(self, nip):
        self.__nip = nip
    def addMarker(self, marker):
        self.__markers.append(marker)
    def addLaptops(self, laptop):
        self.__laptops.append(laptop)
    
    def getNip(self):
        return self.__nip
    def getMarkers(self):
        return self.__markers
    def getLaptops(self):
        return self.__laptops
    
    # method
    def printMarkers(self):
        print("Spidol Punya " + self.getNama())
        i = 0
        for t in self.__markers:
            print(str(i + 1) + ". " + t)
            i += 1
    
    def printLaptops(self):
        print("laptop Punya " + self.getNama())
        i = 0
        for t in self.__laptops:
            print(str(i + 1) + ". " + t)
            i += 1

    def ngajar(self):
        print("jadi gini adik adik..")

    def assignTugas(self):
        print("yah jadi tugas nya adalah..")

    def giveScore(self):
        print("hmm kayanya nilai nya segini deh")
