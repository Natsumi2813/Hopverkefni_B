# Valmynd gert af Kristjáni 22/11/2016 13:22
# Kristján 23/11/2016 09:19
# Guðmundur 29/11/2016 13:56

# Imports
from Lidur1 import *
from Lidur2 import *
from Lidur3 import *
from Lidur4 import *
from Lidur5 import *
from Lidur6 import *
from Lidur7 import *
from korri import *
from time import sleep

def run(lidur):
    if (lidur < 1 or lidur > 8):
        print("Valmöguleikinn er ekki á milli 1 og 8")
        return
    if (lidur == 8):
        print("Slekk á forriti")
        sleep(1)
        quit()
    print("Liður " + str(lidur));
    code = compile("l = Lidur" + str(lidur) + "(); l.Main();", 'fakemodule', 'exec');
    exec(code);

while True:
    # valmyndid
    k = korri()
    k.valmynd()

    x1 = int(input("Veldu valmögu leika: "))

    run(x1)