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
        "FlatHP", "FlatHP", "FlatHP", "FlatHP", "FlatHP", "FlatHP", 
        "PercentHP", "PercentHP", "PercentHP", "PercentHP", 
        "FlatDEF", "FlatDEF", "FlatDEF", "FlatDEF", "FlatDEF", "FlatDEF",
        "PercentDEF", "PercentDEF", "PercentDEF", "PercentDEF", 
        "FlatATK", "FlatATK", "FlatATK", "FlatATK", "FlatATK", "FlatATK", 
        "PercentATK", "PercentATK", "PercentATK", "PercentATK", 
        "EM", "EM", "EM", "EM", 
        "ER", "ER", "ER", "ER", 
        "CR", "CR", "CR", 
        "CD", "CD", "CD"
        ]
    
   

        artifactTypeList = ["Flower", "Feather", "Sands", "Goblet", "Circlet"]

        sandsMainStat = ["PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", "PHP", 
                        "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK", "PATK",  
                        "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", "PDEF", 
                        "EM", "EM", "EM", 
                        "ER", "ER", "ER"]
        # Pyro Hydro Anemo Electro Dendro Cryo Geo
        gobletMainStat = ["PHP", "PATK", "PDEF", "EM", "PHDMG", "PDMG", "HDMG", "ADMG", "EDMG", "DDMG", "CDMG", "GDMG"] #fix
        circletMainStat = ["PHP", "PATK", "PDEF", "EM", "CR", "CD", "HBONUS"] #fix

        StatList = [
        "FlatHP", "FlatHP", "FlatHP", "FlatHP", "FlatHP", "FlatHP", 
        "PercentHP", "PercentHP", "PercentHP", "PercentHP", 
        "FlatDEF", "FlatDEF", "FlatDEF", "FlatDEF", "FlatDEF", "FlatDEF",
        "PercentDEF", "PercentDEF", "PercentDEF", "PercentDEF", 
        "FlatATK", "FlatATK", "FlatATK", "FlatATK", "FlatATK", "FlatATK", 
        "PercentATK", "PercentATK", "PercentATK", "PercentATK", 
        "EM", "EM", "EM", "EM", 
        "ER", "ER", "ER", "ER", 
        "CR", "CR", "CR", 
        "CD", "CD", "CD"
        ]

        

        if type != None:
            type = rand.choice(artifactTypeList)

        # THE CURRENT ASSUMPTION IS A LEVEL 20 ARTIFACT
        if type == "Flower":
            self.mn = "HP"
        elif type == "Feather":
            self.mn = "ATK"
        elif type == "Sands":
            self.mn = rand.choice(sandsMainStat)
        elif type == "Goblet":
            self.mn = rand.choice(gobletMainStat)
        elif type == "Circlet":
            self.mn = rand.choice(circletMainStat)
        
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


    def RandomChooseNumberStat(Substatname):
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