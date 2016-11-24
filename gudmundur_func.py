# Gert af Guðmundi 22/11/2016 13:29

def intInput(text = ""):
    return int(input(text));


def avg(tolur):
    return (sum(tolur) / len(tolur));

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