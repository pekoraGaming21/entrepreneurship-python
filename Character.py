class Character:
    
    elementalDMG = [0,0,0,0,0,0,0,0]
    arts = []

    EM = 0
    ER = 100
    CR = 5
    CD = 50

    def __init__(self, element, bhp, bat, bdf, weaponName, weaponATK, a, ascensionStatName, ascensionStatNumber):
        self.element = element

        self.weapName = weaponName

        self.baseHP = bhp
        self.baseATK = bat + weaponATK
        self.baseDEF = bdf
        self.arts = a

        self.totalHP = self.baseHP
        self.totalATK = self.baseATK
        self.totalDEF = self.baseDEF

        self.CR = 5
        self.CD = 50
        self.EM = 0
        self.ER = 100

        self.ascendName = ascensionStatName
        self.ascendNum = ascensionStatNumber

        for ar in a:
            print(ar)
            self.totalATK += self.getRealValue("ATK", ar.getATK())
            self.totalATK += self.getRealValue("PATK", ar.getPATK()) * self.baseATK

            self.totalDEF += self.getRealValue("DEF", ar.getDEF())
            self.totalDEF += self.getRealValue("PDEF", ar.getPDEF()) * self.baseDEF

            self.totalHP += self.getRealValue("HP", ar.getHP())
            self.totalHP += self.getRealValue("PHP", ar.getPHP()) * self.baseHP

            self.CR += self.getRealValue("CR", ar.getCR())
            self.CD += self.getRealValue("CD", ar.getCD())
            self.EM += self.getRealValue("EM", ar.getEM())
            self.ER += self.getRealValue("ER", ar.getER())

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
            
        if self.ascendName == "HP":
            self.totalHP += self.ascendNum
        elif self.ascendName == "DEF":
            self.totalDEF += self.ascendNum
        elif self.ascendName == "ATK":
            self.totalATK += self.ascendNum
        elif self.ascendName == "PHP":
            self.totalHP += self.ascendNum
        elif self.ascendName == "PDEF":
            self.totalDEF += self.ascendNum
        elif self.ascendName == "PATK":
            self.totalATK += self.ascendNum
        elif self.ascendName == "EM":
            self.EM += self.ascendNum
        elif self.ascendName == "ER":
            self.ER += self.ascendNum
        elif self.ascendName == "CR":
            self.CR += self.ascendNum
        elif self.ascendName == "CD":
            self.CD += self.ascendNum
        elif self.ascendName == "PHDMG":
            self.elementalDMG[0] += self.ascendNum
        elif self.ascendName == "PDMG":
            self.elementalDMG[1] += self.ascendNum
        elif self.ascendName == "HDMG":
            self.elementalDMG[2] += self.ascendNum
        elif self.ascendName == "ADMG":
            self.elementalDMG[3] += self.ascendNum
        elif self.ascendName == "EDMG":
            self.elementalDMG[4] += self.ascendNum
        elif self.ascendName == "DDMG":
            self.elementalDMG[5] += self.ascendNum
        elif self.ascendName == "CDMG":
            self.elementalDMG[6] += self.ascendNum
        elif self.ascendName == "GDMG":
            self.elementalDMG[7] += self.ascendNum

        

    def getRealValue(self, statName, statValue):
        HPList = [209.13, 239.00, 269.88, 298.75]
        PHPList = [0.0408, 0.0466, 0.0525, 0.0583]
        DEFList = [16.20, 18.52, 20.83, 23.15]
        PDEFList = [0.0510, 0.0583, 0.0656, 0.0729]
        ATKList = [13.62, 15.56, 17.51, 19.45]
        PATKList = [0.0408, 0.0466, 0.0525, 0.0583]
        EMList = [16.32, 18.65, 20.98, 23.31]
        ERList = [4.53, 5.18, 5.83, 6.48]
        CRList = [2.72, 3.11, 3.50, 3.89]
        CDList = [5.44, 6.22, 6.99, 7.77]

        RealHPList = self.getRealList(HPList)
        RealPHPList = self.getRealList(PHPList)
        RealDEFList = self.getRealList(DEFList)
        RealPDEFList = self.getRealList(PDEFList)
        RealATKList = self.getRealList(ATKList)
        RealPATKList = self.getRealList(PATKList)
        RealEMList = self.getRealList(EMList)
        RealERList = self.getRealList(ERList)
        RealCRList = self.getRealList(CRList)
        RealCDList = self.getRealList(CDList)

        Reallist = [RealHPList, RealPHPList, RealDEFList, RealPDEFList, RealATKList, RealPATKList, RealEMList, RealERList, RealCRList, RealCDList]
        Stringlist = ["HP", "PHP", "DEF", "PDEF", "ATK", "PATK", "EM", "ER", "CR", "CD"]

        lowestDiff = 100000
        lowestDiffIndex = 0
        for index, realStat in enumerate(Reallist[Stringlist.index(statName)]):
            if abs(statValue - realStat) < lowestDiff:
                lowestDiff = abs(statValue - realStat)
                lowestDiffIndex = index
        return Reallist[Stringlist.index(statName)][lowestDiffIndex]



    def getRealList(self, statValues):
        # make a list of all values
        # check the closest one
        sum = 0
        RealList = [0]
        for i in range(0,4):
            sum += statValues[i]
            if not self.isCloseEnough(sum, RealList):
                RealList.append(sum)
            for j in range(0,4):
                sum += statValues[j]
                if not self.isCloseEnough(sum, RealList):
                    RealList.append(sum)
                for k in range(0,4):
                    sum += statValues[k]
                    if not self.isCloseEnough(sum, RealList):
                        RealList.append(sum)
                    for l in range(0,4):
                        sum += statValues[l]
                        if not self.isCloseEnough(sum, RealList):
                            RealList.append(sum)
                        for m in range(0,4):
                            sum += statValues[m]
                            if not self.isCloseEnough(sum, RealList):
                                RealList.append(sum)
                            for n in range(0,4):
                                sum += statValues[n]
                                if not self.isCloseEnough(sum, RealList):
                                    RealList.append(sum)
                                sum -= statValues[n]
                            sum -= statValues[m]
                        sum -= statValues[l]
                    sum -= statValues[k]
                sum -= statValues[j]
            sum -= statValues[i]
        RealList.sort()
        # print(RealList)

        return RealList


    def isCloseEnough(self, number, list):
        for othernumber in list:
            if abs(number - othernumber) < 0.0001:
                return True
        return False

    def getTotalATK(self):
        return self.totalATK
    

    def getTotalDEF(self):
        return self.totalDEF
    
    def getTotalHP(self):
        return self.totalHP
    
    def getEM(self):
        return self.EM
    
    def getER(self):
        return self.ER
    
    def getCR(self):
        return self.CR
    
    def getCD(self):
        return self.CD
    
    
    