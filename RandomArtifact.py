from Artifact import Artifact
from Substat import Substat
import random as rand
## BIG NOTEEEEEEEEEEEEEEEEEE this will fit into the Artifact.py as a seperate constructor
class RandomArtifact(Artifact):

    def __init__(self, type):

        artifactTypeList = ["Flower", "Feather", "Sands", "Goblet", "Circlet"]

        sandsMainStat = ["PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", 
                        "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK",  
                        "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", 
                        "EM", "EM", "EM", 
                        "ER", "ER", "ER"]
        # Pyro Hydro Anemo Electro Dendro Cryo Geo
        gobletMainStat = ["PHP", "PATK", "PDEF", "EM", "PHDMG", "PDMG", "HDMG", "ADMG", "EDMG", "DDMG", "CDMG", "GDMG"]
        circletMainStat = ["PHP", "PATK", "PDEF", "EM", "CR", "CD", "HBONUS"]

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
    

        if type != None:
            type = rand.choice(artifactTypeList)
        ArtifactMainStatName=""

        # THE CURRENT ASSUMPTION IS A LEVEL 20 ARTIFACT
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
        
        substatlist=self.RemoveSubstat(ArtifactMainStatName, StatList)

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

        print("Main Stat:",ArtifactMainStatName)
        print(substatlist)
        # Remove Main Stat from list of substats to choose
        # Choose substats
        # Determine the initial roll for each substat (for possible testing later)
        # Roll the artifact:
            # Roll 5 times
                #If it's a three stat, turn the -1 4th stat back to 0
                #Else, Choose one substat to roll
                # Add the roll value to the substat
                # Increment its roll count by 1 for easier tracking later
        pass
    #use stat, use for loop to cycle thru the list for finding stat then delete it
    def RemoveSubstat(self, stat, statlist):
        statcount=statlist.count(stat)
        for i in range(statcount):
            statlist.remove(stat)
        return statlist
    

    def RandomChooseNumberStat(self, Substatname):
        HPList = [209.13, 239.00, 269.88, 298.75]
        PHPList = [4.08, 4.66, 5.25, 5.83]
        DEFList = [16.20, 18.52, 20.83, 23.15]
        PDEFList = [5.10, 5.83, 6.56, 7.29]
        ATKList = [13.62, 15.56, 17.51, 19.45]
        PATKList = [4.08, 4.66, 5.25, 5.83]
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
    
    def getType():
        return type