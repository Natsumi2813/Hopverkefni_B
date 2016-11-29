# made by Kristjan O. ragnarsson 24/11/2016

from random import randint
from time import sleep

class gemsla:
    suman = []
    oft7 = 0
    oft12 = 0
    oft3 = 0
    helda = 0
    medaltal = 0

class Lidur7:
    def slembi_tala(self):
        return randint(1, 6)
    def ut_prent(self):
        for i in range(100):
            x1 = self.slembi_tala()
            x2 = self.slembi_tala()
            print("Kast teningur 1 =", x1)
            print("Kast teningur 2 =", x2)
            x3 = (x2 + x1)
            print("Samtals", x3)
            gemsla.suman.append(x3)
            print("Þessi samtal verður settt í lastan sem kast", (i + 1))
            sleep(0.3)
    def hve_oft7(self):
        for i in gemsla.suman:
            if i == 7:
                gemsla.oft7 += 1
    def hve_oft3(self):
        for i in gemsla.suman:
            if i == 3:
                gemsla.oft3 += 1
    def hve_oft12(self):
        for i in gemsla.suman:
            if i == 12:
                gemsla.oft12 += 1
    def heildar_summa(self):
        for i in gemsla.suman:
            gemsla.helda += i
    def medaltal(self):
        gemsla.medaltal = gemsla.helda / 100
    def ut_reikningar(self):
        self.hve_oft12()
        self.hve_oft7()
        self.hve_oft3()
        self.heildar_summa()
        self.medaltal()
    def Main(self):
        self.ut_prent()
        self.ut_reikningar()
        print("Listin óraðaður", *gemsla.suman)
        print("Listin raðaður", sorted(gemsla.suman))
        print("Heildarsumma listans", gemsla.helda)
        print("meðaltal listans", gemsla.medaltal)
        print("summan 7 kom upp", gemsla.oft7, "sinnum")
        print("summan 3 kom upp", gemsla.oft3, "sinnum")
        print("summan 12 kom upp", gemsla.oft12, "sinnum")
        sleep(1)