# Valmynd gert af Kristjáni 22/11/2016 13:22

# Imports
from Lidur1 import *
from Lidur2 import *
from time import sleep

while True:
    # valmyndin
    print("1. Bílar \n2. Samlagning \n3. Skæri, blað, steinn \n4. Strengur \n5. Heiltölur \n6.Teningaspilið Craps"
          "\n7. Teningakast \n8. byggingakast \n9. Hætta")

    x1 = input("Veldu valmögu leika: ")

    if x1 == 1:
        Lidur1.Main()
    elif x1 == 2:
        Lidur2.main()
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