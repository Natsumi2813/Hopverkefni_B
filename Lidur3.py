#Liður 3 - Skæri, blað, steinn. Gert af Guðmundi 22/11/2016 14:00
from gudmundur_func import *
from enum import Enum
from random import randint

class winner(Enum):
    notandi = 0;
    tolva = 1;
    jafntefli = 2;

class Lidur3_data:
    notnadiVann = 0;
    tolvaVann = 0;
    jafntefli = 0;
    leikinn = 0;
    def updateData(self, w):
        self.leikinn = self.leikinn + 1;
        if (w == winner.notandi):
            self.notnadiVann = self.notnadiVann + 1;
            return;
        elif (w == winner.tolva):
            self.tolvaVann = self.tolvaVann + 1;
        elif (w == winner.jafntefli):
            self.jafntefli = self.jafntefli + 1;

class Lidur3:
    data = Lidur3_data();
    def PrintVal(self):
        print("Sláðu inn:");
        print("1. fyrir skæri \n2. fyrir blað\n3. fyrir stein \n4. fyrir að hætta");
    def getCompVal(self):
        return randint(1, 4);
    def processVal(self, val):
        compVal = self.getCompVal();
        if (val == 1 and compVal == 2):
            self.data.updateData(winner.notandi);
        elif (val == 2 and compVal == 1):
            self.data.updateData(winner.tolva);
        elif (val == 2 and compVal == 3):
            self.data.updateData(winner.notandi);
        elif (val == 3 and compVal == 2):
            self.data.updateData(winner.tolva);
        elif (val == 3 and compVal == 1):
            self.data.updateData(winner.notandi);
        elif (val == 1 and compVal == 3):
            self.data.updateData(winner.tolva);
        else:
            self.data.updateData(winner.jafntefli);
    def Main(self):
        while (True):
            self.data = Lidur3_data();
            self.PrintVal();
            val = input(": ");
            if (val == 4):
                break;
            self.processVal();




l = Lidur3();
l.Main();