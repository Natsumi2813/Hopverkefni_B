# Gert af Guðmundi 22/11/2016 13:29

def intInput(text = ""):
    return int(input(text));


def avg(tolur):
    return (sum(tolur) / len(tolur));


def endurtaka(texti="Villtu endurtaka þetta: "):
    svar = "";
    while (True):
        if (svar != ""):
            print(svar + " er ekki gilt svar!");
        svar = input(texti).lower();
        if ("já" in svar or "nei" in svar):
            break;
    return ("já" in svar);

class String(str):
    def ToInt(self):
        return int(self);
    def repAllExcept(self, chars, w):
        tmpStr = String();
        for i in range(len(self)):
            if (self[i] in chars):
                tmpStr = tmpStr + self[i];
            else:
                tmpStr = tmpStr + "*";
        return tmpStr;