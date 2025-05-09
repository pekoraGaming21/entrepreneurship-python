class Character:
    elementalDMG = [0,0,0,0,0,0,0,0]
    arts = []

    EM = 0
    ER = 0
    CR = 0
    CD = 0

    def __init__(self, bhp, bat, bdf, a):
        self.baseHP = bhp
        self.baseATK = bat
        self.baseDEF = bdf
        self.arts = a

        self.totalHP = bhp
        self.totalATK = bat
        self.totalDEF = bdf

        for ar in a:
            print(ar)
            self.totalATK += ar.getATK(self.baseATK)
            self.totalDEF += ar.getDEF(self.baseDEF)
            self.totalHP += ar.getHP(self.baseHP)

            # print(self.totalATK)
            temp = ar.getMain()
            if temp == "HP":
                self.totalHP += ar.getMainV()
            elif temp == "DEF":
                self.totalDEF += ar.getMainV()
            elif temp == "ATK":
                self.totalATK += ar.getMainV()
            elif temp == "PHP":
                self.totalHP += ar.getMainV() * self.baseHP
            elif temp == "PDEF":
                self.totalDEF += ar.getMainV() * self.baseDEF
            elif temp == "PATK":
                self.totalATK += ar.getMainV() * self.baseATK
            elif temp == "EM":
                self.EM += ar.getMainV()
            elif temp == "ER":
                self.ER += ar.getMainV()
            elif temp == "CR":
                self.CR += ar.getMainV()
            elif temp == "CD":
                self.CD += ar.getMainV()
            elif temp == "PHDMG":
                self.elementalDMG[0] += ar.getMainV()
            elif temp == "PDMG":
                self.elementalDMG[1] += ar.getMainV()
            elif temp == "HDMG":
                self.elementalDMG[2] += ar.getMainV()
            elif temp == "ADMG":
                self.elementalDMG[3] += ar.getMainV()
            elif temp == "EDMG":
                self.elementalDMG[4] += ar.getMainV()
            elif temp == "DDMG":
                self.elementalDMG[5] += ar.getMainV()
            elif temp == "CDMG":
                self.elementalDMG[6] += ar.getMainV()
            elif temp == "GDMG":
                self.elementalDMG[7] += ar.getMainV()
            
            # print(self.totalATK)
            # print(self.totalDEF)
            # print(self.totalHP)


    def getTotalATK(self):
        return self.totalATK
    

    def getTotalDEF(self):
        return self.totalDEF
    
    def getTotalHP(self):
        return self.totalHP