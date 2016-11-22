#Liður 1 - bílar.  Gert af Guðmundi 22/11/2016 13:24
from gudmundur_func import *

class Lidur1:
    def fjoldiBila(self, fjoldi):
        return (fjoldi // 5) + 1;
    def fjoldiISidasta(self, fjoldi):
        return (fjoldi%5)
    def Main(self):
        fjoldi = intInput("Hvað eru margir skráðir í ferðina? ");
        if (fjoldi >= 5):
            print("Fjöldi bíla sem þarf: " + str(self.fjoldiBila(fjoldi)));
            print("Fjöldi í síðasta bílnum: " + str(self.fjoldiISidasta(fjoldi)));
        else:
            print("Því miður eru ekki nógu margir skráðir, hætt er við ferðina.");
