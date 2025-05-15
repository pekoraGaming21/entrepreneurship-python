from Artifact import Artifact
from Substat import Substat
import random as rand
## BIG NOTEEEEEEEEEEEEEEEEEE this will fit into the Artifact.py as a seperate constructor
class RandomArtifact(Artifact):

    def __init__(self, type):
        # THE CURRENT ASSUMPTION IS A LEVEL 20 ARTIFACT

        # Initilize Lists. Lists have built in accurate proability, such that a random chosen stat matches in-game odds.
        artifactTypeList = ["Flower", "Feather", "Sands", "Goblet", "Circlet"]

        sandsMainStat = ["PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", 
                        "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK",  
                        "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", 
                        "EM", "EM", "EM", 
                        "ER", "ER", "ER"]
        gobletMainStat = self.getGobletList()
        circletMainStat = ["PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", 
                           "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", 
                           "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", 
                           "EM", "EM", 
                           "CR", "CR", "CR", "CR", "CR", 
                           "CD", "CD", "CD", "CD", "CD", 
                           "HBONUS", "HBONUS", "HBONUS", "HBONUS", "HBONUS"]

        StatList = [
        "HP", "HP", "HP", "HP", "HP", "HP", 
        "PHP", "PHP", "PHP", "PHP", 
        "DEF", "DEF", "DEF", "DEF", "DEF", "DEF",
        "PDEF", "PDEF", "PDEF", "PDEF", 
        "ATK", "ATK", "ATK", "ATK", "ATK", "ATK", 
        "PATK", "PATK", "PATK", "PATK", 
        "EM", "EM", "EM", "EM", 
        "ER", "ER", "ER", "ER", 
        "CR", "CR", "CR", 
        "CD", "CD", "CD"
        ]
    
        # If a specific type of artifact wasn't given, then make a random type
        if type == None:
            type = rand.choice(artifactTypeList)
        ArtifactMainStatName=""

        # Set the Main Stat Name
        if type == "Flower":
            ArtifactMainStatName = "HP"
        elif type == "Feather":
            ArtifactMainStatName = "ATK"
        elif type == "Sands":
            ArtifactMainStatName = rand.choice(sandsMainStat)
        elif type == "Goblet":
            ArtifactMainStatName = rand.choice(gobletMainStat)
        elif type == "Circlet":
            ArtifactMainStatName = rand.choice(circletMainStat)
        
        # Remove Main Stat from possible substats
        substatlist=self.RemoveSubstat(ArtifactMainStatName, StatList)

        # Choose a random substat. Remove that substat from possible substats (to prevent same substat from being chosen again)
        substat1name=rand.choice(StatList)
        substat1value=self.RandomChooseNumberStat(substat1name)
        substatlist=self.RemoveSubstat(substat1name, substatlist)

        substat2name=rand.choice(StatList)
        substat2value=self.RandomChooseNumberStat(substat2name)
        substatlist=self.RemoveSubstat(substat2name, substatlist)

        substat3name=rand.choice(StatList)
        substat3value=self.RandomChooseNumberStat(substat3name)
        substatlist=self.RemoveSubstat(substat3name, substatlist)

        substat4name=rand.choice(StatList)
        substat4value=self.RandomChooseNumberStat(substat4name)
        substatlist=self.RemoveSubstat(substat4name, substatlist)

        # Set rollcounts. Will be helpful and QOL
        substat1roll = 0
        substat2roll = 0
        substat3roll = 0
        substat4roll = -1

         # Determine 3 or 4 liner artifact
        if rand.random() > 0.8:
            substat4roll = 0
        
        # Roll the artifact 5 times
        for i in range(5):
            # If a 3 liner, the first roll adds the 4th stat
            if substat4roll == -1:
                substat4roll = 0
            else:
                # Pick one of four substats. Add their respective possible substat value and increment the roll count
                statRoll = rand.randint(1,4)
                if statRoll == 1:
                    substat1roll += 1
                    substat1value += self.RandomChooseNumberStat(substat1name)
                if statRoll == 2:
                    substat2roll += 1
                    substat2value += self.RandomChooseNumberStat(substat2name)
                if statRoll == 3:
                    substat3roll += 1
                    substat3value += self.RandomChooseNumberStat(substat3name)
                if statRoll == 4:
                    substat4roll += 1
                    substat4value += self.RandomChooseNumberStat(substat4name)

        print("Type:", type)
        print("Main Stat:", ArtifactMainStatName)
        print("")
        print("(" + str(substat1roll) + ") " + substat1name + " -", str(substat1value))
        print("(" + str(substat2roll) + ") " + substat2name + " -", str(substat2value))
        print("(" + str(substat3roll) + ") " + substat3name + " -", str(substat3value))
        print("(" + str(substat4roll) + ") " + substat4name + " -", str(substat4value))

        # Actually set the object's stats
        self.type = type
        self.main = ArtifactMainStatName
        self.mainValue = round(self.getMainStatNumber(ArtifactMainStatName, 20), 4)
        self.substats = [0,0,0,0]
        self.substats[0] = Substat(substat1name, round(substat1value, 4))
        self.substats[1] = Substat(substat2name, round(substat2value, 4))
        self.substats[2] = Substat(substat3name, round(substat3value, 4))
        self.substats[3] = Substat(substat4name, round(substat4value, 4))

    def RemoveSubstat(self, stat, statlist):
        # Given the name of the stat and the stalist: 
    
        # Remove a stat completely from the statlist
        statcount=statlist.count(stat)
        for i in range(statcount):
            statlist.remove(stat)
        return statlist
    
    def RandomChooseNumberStat(self, Substatname):
        # Given the name of substat

        # Return a random possible substat value
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

        if (Substatname == "HP"):
            return rand.choice(HPList)
        elif (Substatname == "PHP"):
            return rand.choice(PHPList)
        elif (Substatname == "DEF"):
            return rand.choice(DEFList)
        elif (Substatname == "PDEF"):
            return rand.choice(PDEFList)
        elif (Substatname == "ATK"):
            return rand.choice(ATKList)
        elif (Substatname == "PATK"):
            return rand.choice(PATKList)
        elif (Substatname == "EM"):
            return rand.choice(EMList)
        elif (Substatname == "ER"):
            return rand.choice(ERList)
        elif (Substatname == "CR"):
            return rand.choice(CRList)
        elif (Substatname == "CD"):
            return rand.choice(CDList)
        return -1
    
    def getMainStatNumber(self, statname, level):
        # Given the stat name and level of artifact

        # Return the appropriate Main Stat Value
        if statname == "HP":
            return 4780
        elif statname == "ATK":
            return 311
        elif statname == "PHP" or statname == "PATK":
            return 0.466
        elif statname == "PDEF" or statname == "PHDMG":
            return 0.583
        elif statname == "EM":
            return 186.5
        elif statname == "ER":
            return 51.8
        elif statname == "PDMG" or statname == "HDMG" or statname == "ADMG" or statname == "EDMG" or statname == "DDMG" or statname == "CDMG" or statname == "GDMG":
            return 0.466
        elif statname == "CR":
            return 31.1
        elif statname == "CD":
            return 62.2
        elif statname == "HBONUS":
            return 0.359
        return -1
    
    def getGobletList(self):
        # Create the built-in probability list for goblet types
        returnList = []

        for i in range(400):
            if i < 77:
                returnList.append("PHP")
            elif i < 154:
                returnList.append("PATK")
            elif i < 230:
                returnList.append("PDEF")
            elif i < 250:
                returnList.append("PHDMG")
            elif i < 270:
                returnList.append("PDMG")
            elif i < 290:
                returnList.append("HDMG")
            elif i < 310:
                returnList.append("ADMG")
            elif i < 330:
                returnList.append("EDMG")
            elif i < 350:
                returnList.append("DDMG")
            elif i < 370:
                returnList.append("CDMG")
            elif i < 390:
                returnList.append("GDMG")
            elif i < 400:
                returnList.append("EM")
        return returnList
    
    # def printArtifact(ArtifactMainStatName):
    #     print("Type:", type)
    #     print("Main Stat:", ArtifactMainStatName)
    #     print("")
    #     print("(" + str(substat1roll) + ") " + substat1name + " -", str(substat1value))
    #     print("(" + str(substat2roll) + ") " + substat2name + " -", str(substat2value))
    #     print("(" + str(substat3roll) + ") " + substat3name + " -", str(substat3value))
    #     print("(" + str(substat4roll) + ") " + substat4name + " -", str(substat4value))
    
    def getType():
        return type