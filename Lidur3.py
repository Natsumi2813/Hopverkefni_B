#Liður 3 - Skæri, blað, steinn. Gert af Guðmundi 22/11/2016 14:00
#edit 24/11/2016
from gudmundur_func import *
from enum import Enum
from random import randint

class winner(Enum):
    notandi = 0;
    tolva = 1;
    jafntefli = 2;

class Lidur3_data:
    # classi til þess að geyma gögn í
    notnadiVann = 0;
    tolvaVann = 0;
    jafntefli = 0;
    leikinn = 0;
    nafn = "";
    aldur = 0;
    def setNafnOgAldur(self, nafn, aldur):
        #setur nafn og aldur breyturnar
        self.nafn = nafn;
        self.aldur = aldur;
    def update(self, w):
        self.leikinn = self.leikinn + 1;
        if (w == winner.notandi):
            self.notnadiVann = self.notnadiVann + 1;
            return;
        elif (w == winner.tolva):
            self.tolvaVann = self.tolvaVann + 1;
            return;
        elif (w == winner.jafntefli):
            self.jafntefli = self.jafntefli + 1;
            return;

class Lidur3:
    data = Lidur3_data();
    def PrintVal(self):
        #prenstar út valmyndina
        print("Sláðu inn:");
        print("1. fyrir skæri \n2. fyrir blað\n3. fyrir stein \n4. fyrir að hætta");
    def getCompVal(self):
        #returnar því sem tölvan velur
        return randint(1, 3);
    def printWin(self, w):
        #prentar út hann sem vann
        if (w == winner.notandi):
            print("Þú vannst");
        elif (w == winner.tolva):
            print ("Tölvan vann!");
    def getCompValStr(self, val):
        #returnar strengi sem segir hvað tölvan valdi
        if (val == 1):
            return "Tölvan valdi skæri";
        elif (val == 2):
            return "Tölvan valdi blað";
        elif (val == 3):
            return "Tölvan valdi stein";
    def processVal(self, val):
        compVal = self.getCompVal();
        print(self.getCompValStr(compVal));
        if (val == 1 and compVal == 2):
            self.printWin(winner.notandi);
            self.data.update(winner.notandi);
        elif (val == 2 and compVal == 1):
            self.printWin(winner.tolva);
            self.data.update(winner.tolva);
        elif (val == 2 and compVal == 3):
            self.printWin(winner.notandi);
            self.data.update(winner.notandi);
        elif (val == 3 and compVal == 2):
            self.printWin(winner.tolva);
            self.data.update(winner.tolva);
        elif (val == 3 and compVal == 1):
            self.printWin(winner.notandi)
            self.data.update(winner.notandi);
        elif (val == 1 and compVal == 3):
            self.printWin(winner.tolva);
            self.data.update(winner.tolva);
        else:
            print("Það er jafntefli");
            self.data.update(winner.jafntefli);
    def printStig(self):
        print("Þú heitir " + self.data.nafn + " og þú ert " + str(self.data.aldur)  + " ára");
        print("Þú vannst " + str(self.data.notnadiVann) + " sinnum");
        print("Tölvan vann " + str(self.data.tolvaVann) + " sinnum");
        print("Það var jafntefli " + str(self.data.jafntefli) + " sinnum");
        print("Leikurinn var spilaður " + str(self.data.leikinn) + " sinnum");
    def Main(self):
        self.data = Lidur3_data();
        self.data.setNafnOgAldur(input("Sláðu inn nafnið þitt: "), intInput("Sláðu inn aldurinn þinn: "));
        while (True):
            self.PrintVal();
            val = intInput(": ");
            if (val == 4):
                if (self.data.leikinn > 0):
                    self.printStig();
                break;
            self.processVal(val);