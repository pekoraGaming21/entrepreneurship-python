from Substat import Substat


class Artifact:
    def __init__(self, type, mn, mstat, one, two, three, four=None):
        if four is None:
            self.type = type
            self.main = mn
            self.mainValue = mstat
            self.substats = [0,0,0,None]
            self.substats[0] = one
            self.substats[1] = two
            self.substats[2] = three
        else:
            self.type = type
            self.main = mn
            self.mainValue = mstat
            self.substats = [0,0,0,0]
            self.substats[0] = one
            self.substats[1] = two
            self.substats[2] = three
            self.substats[3] = four
            return

    def __str__(self):
        return(f"Main: {self.main}, {self.mainValue}\n{self.substats[0]}, {self.substats[1]}, {self.substats[2]}, {self.substats[3]}")

    def getType(self):
        return self.type

    def getSubstat1(self):
        return self.substats[0]
    
    def getSubstat2(self):
        return self.substats[1]

    def getSubstat3(self):
        return self.substats[2]

    def getSubstat4(self):
        return self.substats[3]

    def setSubstat4(self, substat):
        self.substats[3] = substat

    def setSubstat1Value(self, value):
        self.substats[0].setValue(value)

    def getMain(self):
        return self.main
    
    def getMainV(self):
        return self.mainValue
    
    def getATK(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "ATK":
                returner += s.getValue()
        return returner
    
    def getPATK(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "PATK":
                returner += s.getValue()
        return returner

    def getDEF(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "DEF":
                returner += s.getValue()
        return returner
    
    def getPDEF(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "PDEF":
                returner += s.getValue()
        return returner

    def getHP(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "HP":
                returner += s.getValue()
        return returner
    
    def getPHP(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "PHP":
                returner += s.getValue()
        return returner
    
    def getEM(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "EM":
                returner += s.getValue()
        return returner

    def getER(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "ER":
                returner += s.getValue()
        return returner

    def getCR(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "CR":
                returner += s.getValue()
        return returner
    
    def getCD(self):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == "CD":
                returner += s.getValue()
        return returner

    def getElemental(self):
        for s in self.substats:
            if "PHDMG, PDMG, HDMG, ADMG, EDMG, DDMG, CDMG, GDMG".find(s.getStat()) > 0:
                return s.getStat
        return "Something went wrong in getElemental"
    
    def getELementalDMG(self, element):
        returner = 0.0
        for s in self.substats:
            if s.getStat() == element:
                returner += s.getValue()
        return returner