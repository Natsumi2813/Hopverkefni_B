# Valmynd gert af Kristjáni 22/11/2016 13:22
# Kristján 23/11/2016 09:19

# Imports
from Lidur1 import *
from Lidur2 import *
from Lidur3 import *
from Lidur4 import *
from Lidur5 import *
from Lidur7 import *
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
        print("Lidur 3")
        l3 = Lidur3()
        l3.Main()
    elif x1 == 4:
        print("lidur 4")
        l4 = Lidur4()
        l4.main()
    elif x1 == 5:
        print("lidur 5")
        l5 = Lidur5()
        l5.Main()
    elif x1 == 6:
        print()
    elif x1 == 7:
        print("Lidur 7")
        l7 = Lidur7()
        l7.main()
    elif x1 == 8:
        print("Slekk á forriti")
        sleep(1)
        quit()