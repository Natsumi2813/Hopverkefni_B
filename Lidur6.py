#Liður 6 - Teningaspilið Craps.  Gert af Guðmundi 24/11/2016 11:47
from  gudmundur_func import *
from random import randint
from time import sleep

class Teningur:
    hlid = 0;
    def kasta(self):
        self.hlid = randint(1, 6);

class Lidur6_geymsla:
    teningur1 = Teningur();
    teningur2 = Teningur();
    stig = 0;
    fyrstaKastStig = 0;

class Lidur6:
    geymsla = Lidur6_geymsla();

    def KastaTeningum(self):
        self.geymsla.teningur1.kasta();
        print("Þú fékkst " + self.teningur1.hlid + " á fyrsta teningnum");
        sleep(1);
        self.geymsla.teningur2.kasta();
        print("Þú fékkst " + self.teningur2.hlid + " á seinni teningnum");

    def FyrstaKast(self):
        self.KastaTeningum();
        summa = self.teningur1.hlid + self.teningur2.hlid;
        if (summa in [7, 11]):
            print("Þú vannst af því að summan var" + str(summa));
            return True;
        if (summa in [4, 5, 6, 8, 9, 10]):
            self.geymsla.stig = summa;
            self.geymsla.fyrstaKastStig = summa;
            return False;
        if (summa in [2, 3, 12 ]):
            print("Þú tapaðir af því að þú varst með " + str(summa));
            return True;

    def Main(self):
        print("******Craps******");
        while (True):
            self.geymsla = Lidur6_geymsla();
            while (True):
                if (self.FyrstaKast()):
                    break;

            if (not endurtaka("Villtu spila leikinn aftur")):
                break;
