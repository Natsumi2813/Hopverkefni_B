# lidur 2 gert af Kristjáni 22/11/2016
# Kristján 23/11/2016 09:19
def neg(x):
    abs(x)
    return(-x)

class Lidur2:
    def upp(self, x):
        summan = 0
        for i in range(x):
            summan += (i + 1)
            if i >= 1:
                print(" +", i + 1, end="")
            else:
                print(i + 1, end="")
        print(" Gefur töluna", summan)
    def nidur(self, x):
        summa = 0
        for i in range(x, 0):
            summa += x
            if i != -1:
                print(" ("+str(i)+") +", end="")
            else:
                print(" (-1)", end="")
        print(" Gefur töluna", neg(summa))
    def main(self):
        x1 = int(input("Sláðu inn tölu: "))
        if x1 == 0:
            print("Takk fyrir að nota forritið")
            quit()
        elif x1 > 0:
            self.upp(x1)
        elif x1 < 0:
            self.nidur(x1)


