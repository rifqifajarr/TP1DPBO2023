class Human:
    # kelas untuk menampung data human dan method mangan

    # atribut
    __jenisKelamin = ""
    __nama = ""

    # konstruktor
    def __init__(self):
        self.__jenisKelamin = ""
        self.__nama = ""

    # setter getter
    def setjenisKelamin(self, jenisKelamin):
        self.__jenisKelamin = jenisKelamin
    def setNama(self, nama):
        self.__nama = nama
    
    def getjenisKelamin(self):
        return self.__jenisKelamin
    def getNama(self):
        return self.__nama
    
    # method
    def makan(self):
        print("oke mangan..")

    def minum(self):
        print("oke minum..")

    def tidur(self):
        print("one eye open when i sleep")
