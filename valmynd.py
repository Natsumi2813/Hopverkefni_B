# Valmynd gert af Kristjáni 22/11/2016 13:22

# Imports
from Lidur1 import *
from Lidur2 import *
from korri import *
from time import sleep

while True:
    # valmyndid
    k = korri()
    k.valmynd()

    x1 = int(input("Veldu valmögu leika: "))

    if x1 == 1:
        print("Lidur 1")
        l = Lidur1()
        l.Main()
    elif x1 == 2:
        print("Lidur 2")
        l2 = Lidur2()
        l2.main()
    elif x1 == 3:
        print()
    elif x1 == 4:
        print()
    elif x1 == 5:
        print()
    elif x1 == 6:
        print()
    elif x1 == 7:
        print()
    elif x1 == 8:
        print()
    elif x1 == 9:
        print("Slekk á forriti")
        sleep(1)
        quit()