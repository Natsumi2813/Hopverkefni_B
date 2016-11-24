#Liður 5 - Heiltölur. Gert af Guðmundi
from gudmundur_func import *

class Lidur5:

    def Main(self):
        tolur = [];
        for i in range(7):
            tolur.append(intInput("Sláðu inn tölu " + str(i + 1) + ": "));
        print("Minnsta talan er "+ str(min(tolur)));
        print("Stærsta talan er " + str(max(tolur)));
        print("Summa talnanna er " + str(sum(tolur)));
        print("Meðaltal talnanna er " + str(int(avg(tolur))));