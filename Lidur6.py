#Liður 6 - Teningaspilið Craps.  Gert af Guðmundi 24/11/2016 11:47
from  gudmundur_func import *
from random import randint
from time import sleep

class Teningur:
    #teninga classinn
    hlid = 0;
    def kasta(self):
        self.hlid = randint(1, 6);

class Lidur6_geymsla:
    #classi til að geyma teningana og stigin
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
        #katar báðum teningunum
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
        #returnar summu tenings 1 ig tenings 2
        return (self.geymsla.teningur1.hlid + self.geymsla.teningur2.hlid);

    def Main(self):
        print("******Craps******");
        while (True):
            #búa til nýtt instance af Lidur6_geymsla til þess að reseta allar breiturnar
            self.geymsla = Lidur6_geymsla();
            while (True):
                if (self.summaTeninganna() != 0):
                    # Fara út úr while loopinu ef það er búið að kasta teningi
                    break;
                if (self.FyrstaKast()):
                    # Fara út úr while loopinu ef notandinn tapaði
                    break;
                while (True):
                    self.KastaTeningum();
                    if (self.summaTeninganna() == self.geymsla.fyrstaKastStig):
                        #ef stigin eru jafn mörg í fyrsta kasti
                        print("Þú vannst");
                        break;
                    if (self.summaTeninganna() == 7):
                        print("Þú tapaðir");
                        break;

            if (not endurtaka("Villtu spila leikinn aftur: ")):
                break;