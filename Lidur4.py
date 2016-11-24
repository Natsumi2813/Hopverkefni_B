# gert af Kristjáni 24/11/2016

class Lidur4:
    def breiti_streng(self, x):
        for i in ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "t", "u", "v", "w",
                  "x", "y", "z", "á", "ó", "ö", "í", "ú", "ý", "é", "ð", "þ", "æ", "B", "C", "D", "E", "F", "G", "H",
                  "I", "J", "K", "L", "M", "O", "Ó", "P", "Q", "R", "T", "U", "V", "W", "X", "Y", "Z", "Á", "Ö", "Í",
                  "Ú", "Ý", "É", "Ð", "Þ", "Æ"]:
            if i in x:
                x = x.replace(i, '*')
        return x
    def main(self):
        x = str(input("Sláðu inn setningu: "))
        print(self.breiti_streng(x))


