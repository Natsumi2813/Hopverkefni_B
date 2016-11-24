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

    def __init__(self):
        self.teningur1 = Teningur();
        self.teningur2 = Teningur();
        self.stig = 0;
        self.fyrstaKastStig = 0;

class Lidur6:
    geymsla = Lidur6_geymsla();

    def KastaTeningum(self):
        input("Ýttu á enter til að kasta fyrri teningnum");
        self.geymsla.teningur1.kasta();
        print("Þú fékkst " + str(self.geymsla.teningur1.hlid) + " á fyrsta teningnum");
        input("Ýttu á enter til að kasta seinni teningnum");
        self.geymsla.teningur2.kasta();
        print("Þú fékkst " + str(self.geymsla.teningur2.hlid) + " á seinni teningnum");
        print("Summan þín er " + str(self.summaTeninganna()))

    def FyrstaKast(self):
        self.KastaTeningum();
        summa = self.summaTeninganna();
        if (summa in [7, 11]):
            print("Þú vannst");
            return True;
        if (summa in [4, 5, 6, 8, 9, 10]):
            print("Summan bættist við stigin þín");
            self.geymsla.stig = summa;
            self.geymsla.fyrstaKastStig = summa;
            return False;
        if (summa in [2, 3, 12 ]):
            print("Þú tapaðir");
            return True;

    def summaTeninganna(self):
        return (self.geymsla.teningur1.hlid + self.geymsla.teningur2.hlid);

    def Main(self):
        print("******Craps******");
        while (True):
            self.geymsla = Lidur6_geymsla();
            while (True):
                if (self.summaTeninganna() != 0):
                    break;
                if (self.FyrstaKast()):
                    break;
                while (True):
                    self.KastaTeningum();
                    if (self.summaTeninganna() == self.geymsla.fyrstaKastStig):
                        print("Þú vannst");
                        break;
                    if (self.summaTeninganna() == 7):
                        print("Þú tapaðir");
                        break;

            if (not endurtaka("Villtu spila leikinn aftur: ")):
                break;