import random as rand
from Calculator import Calculator
from Artifact import Artifact
from Substat import Substat
from Character import Character

class NewArtifactProbability:

    def __init__(self, newArtifact, character, level):
        self.newArtifact = newArtifact
        self.character = character
        self.level = level
        print("Begin New Artifact test")

    def Probability(self):
        FirstDegreePossibleArtifacts = []
        SecondDegreePossibleArtifacts = []
        ThirdDegreePossibleArtifacts = []
        FourthDegreePossibleArtifacts = []

        BetterArtifacts = []

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
        
        

            
        if self.newArtifact.getSubstat4() != None:
            ZeroDegreePossibleArtifacts = [self.newArtifact]
            # NewList = []
            # for sub in range(1,5):
            #     for stat in range(4):
            #         if sub == 1:
                                               
            #             Adding = self.ChooseNumberStat(self.newArtifact.getSubstat1().getStat(), stat)
                        
            #             self.newArtifact.setSubstat1Value(self.newArtifact.getSubstat1().getValue() + Adding)

            #             addArtifact = Artifact(self.newArtifact.getType(), self.newArtifact.getMain(), self.newArtifact.getMainV(), Substat(self.newArtifact.getSubstat1().getStat(), self.newArtifact.getSubstat1().getValue() + Adding), self.newArtifact.getSubstat2(), self.newArtifact.getSubstat3(), self.newArtifact.getSubstat4())
                        
            #             NewList.append(addArtifact)
                        
            #             self.newArtifact.setSubstat1Value(self.newArtifact.getSubstat1().getValue() - Adding)
                        
            #         if sub == 2:
            #             Adding = self.ChooseNumberStat(self.newArtifact.getSubstat2().getStat(), stat)
            #             self.newArtifact.getSubstat2().setValue(self.newArtifact.getSubstat2().getValue() + Adding)

                        

            #             addArtifact = Artifact(self.newArtifact.getType(), self.newArtifact.getMain(), self.newArtifact.getMainV(), self.newArtifact.getSubstat1(), self.newArtifact.getSubstat2(), self.newArtifact.getSubstat3(), self.newArtifact.getSubstat4())
            #             print("Adding Artifact: ")
            #             print(addArtifact)
            #             NewList.append(addArtifact)
            #             self.newArtifact.getSubstat2().setValue(self.newArtifact.getSubstat2().getValue() - Adding)
            #         if sub == 3:
            #             Adding = self.ChooseNumberStat(self.newArtifact.getSubstat3().getStat(), stat)
            #             self.newArtifact.getSubstat3().setValue(self.newArtifact.getSubstat3().getValue() + Adding)

            #             print(self.newArtifact.getSubstat3().getValue())

            #             addArtifact = Artifact(self.newArtifact.getType(), self.newArtifact.getMain(), self.newArtifact.getMainV(), self.newArtifact.getSubstat1(), self.newArtifact.getSubstat2(), self.newArtifact.getSubstat3(), self.newArtifact.getSubstat4())

            #             NewList.append(addArtifact)
            #             self.newArtifact.getSubstat3().setValue(self.newArtifact.getSubstat3().getValue() - Adding)
            #         if sub == 4:
            #             Adding = self.ChooseNumberStat(self.newArtifact.getSubstat4().getStat(), stat)
            #             self.newArtifact.getSubstat4().setValue(self.newArtifact.getSubstat4().getValue() + Adding)

            #             addArtifact = Artifact(self.newArtifact.getType(), self.newArtifact.getMain(), self.newArtifact.getMainV(), self.newArtifact.getSubstat1(), self.newArtifact.getSubstat2(), self.newArtifact.getSubstat3(), self.newArtifact.getSubstat4())

            #             NewList.append(addArtifact)
            #             self.newArtifact.getSubstat4().setValue(self.newArtifact.getSubstat4().getValue() - Adding)

            # print("END, printing all artifacts in new list")
            # for artifact in NewList:
            #     print(artifact)


                     
            FirstDegreePossibleArtifacts = self.CreateDegreeListPossibleArtifact(ZeroDegreePossibleArtifacts)
            SecondDegreePossibleArtifacts = self.CreateDegreeListPossibleArtifact(FirstDegreePossibleArtifacts)
            ThirdDegreePossibleArtifacts = self.CreateDegreeListPossibleArtifact(SecondDegreePossibleArtifacts)
            FourthDegreePossibleArtifacts = self.CreateDegreeListPossibleArtifact(ThirdDegreePossibleArtifacts)
            FifthDegreePossibleArtifacts = self.CreateDegreeListPossibleArtifact(FourthDegreePossibleArtifacts)
            
            

            ArtifactBetterCounter = 0
            ArtifactTotalCounter = 0
            print("Fifth Degree Possible Artifacts size:")
            print(len(FifthDegreePossibleArtifacts))
            for artifact in FifthDegreePossibleArtifacts:
                ArtifactTotalCounter += 1
                if ArtifactTotalCounter % 1000 == 0:
                    print(ArtifactTotalCounter)
                if self.isBetterArtifact(artifact, artifact.getType(), self.character):
                    ArtifactBetterCounter += 1
                    BetterArtifacts.append(artifact)
                    

            print("Num Better Artifacts: " + str(ArtifactBetterCounter))
            for artifact in BetterArtifacts:
                print(artifact)
            return ArtifactBetterCounter / len(FifthDegreePossibleArtifacts)


        elif self.newArtifact.getSubstat4() == None:

            pass
            




            pass

        else:
            print("tf how did this happen")
        
       
        
        # If newArtifact has 3 stats
        # First roll creates the 4th stat
        # Roll the newArtifact 4 times
        # # Cycle through: Choose first sub add first stat, choose first sub add 2nd stat
        
    def CreateDegreeListPossibleArtifact(self, PastList):
        NewList = []
        for testArtifact in PastList:
            
            for sub in range(1,5):
                for stat in range(4):
                    if sub == 1:       
                    
                        Adding = self.ChooseNumberStat(testArtifact.getSubstat1().getStat(), stat)
                        
                        addArtifact = Artifact(testArtifact.getType(), testArtifact.getMain(), testArtifact.getMainV(), Substat(testArtifact.getSubstat1().getStat(), testArtifact.getSubstat1().getValue() + Adding), testArtifact.getSubstat2(), testArtifact.getSubstat3(), testArtifact.getSubstat4())
                        
                        NewList.append(addArtifact)
                        
                        
                    elif sub == 2:
                        Adding = self.ChooseNumberStat(testArtifact.getSubstat2().getStat(), stat)

                        addArtifact = Artifact(testArtifact.getType(), testArtifact.getMain(), testArtifact.getMainV(), testArtifact.getSubstat1(), Substat(testArtifact.getSubstat2().getStat(), testArtifact.getSubstat2().getValue() + Adding), testArtifact.getSubstat3(), testArtifact.getSubstat4())

                        NewList.append(testArtifact)
                    elif sub == 3:
                        Adding = self.ChooseNumberStat(testArtifact.getSubstat3().getStat(), stat)
                        addArtifact = Artifact(testArtifact.getType(), testArtifact.getMain(), testArtifact.getMainV(), testArtifact.getSubstat1(), testArtifact.getSubstat2(), Substat(testArtifact.getSubstat3().getStat(), testArtifact.getSubstat3().getValue() + Adding), testArtifact.getSubstat4())

                        NewList.append(testArtifact)
                    elif sub == 4:
                        Adding = self.ChooseNumberStat(testArtifact.getSubstat1().getStat(), stat)
                        addArtifact = Artifact(testArtifact.getType(), testArtifact.getMain(), testArtifact.getMainV(), testArtifact.getSubstat1(), testArtifact.getSubstat2(), testArtifact.getSubstat3(), Substat(testArtifact.getSubstat4().getStat(), testArtifact.getSubstat4().getValue() + Adding))

                        NewList.append(testArtifact)
        
        return NewList

    def isBetterArtifact(self, artifact, artifactType, character):
        oldArtifact = self.character.getArtifact(artifactType)
        

        damage = Calculator()
        damage.setBase(self.character.getTotalATK() * 1.50, 1, 0)
        damage.setBonus(0, self.character.getElement(), "Anemo", self.character.getElementalDMG("Anemo"))
        damage.setTarget(103, 90, 0.1, 0)
        damage.setAmp(self.character.getEM(), "None", 0)
        damage.setCritDMG("Average", self.character.getCR(), self.character.getCD())
        oldDamage = damage.calculate()

        
        self.character.setArtifact(artifactType, artifact)

        damage.setBase(self.character.getTotalATK() * 1.50, 1, 0)
        damage.setBonus(0, self.character.getElement(), "Anemo", self.character.getElementalDMG("Anemo"))
        damage.setTarget(103, 90, 0.1, 0)
        damage.setAmp(self.character.getEM(), "None", 0)
        damage.setCritDMG("Average", self.character.getCR(), self.character.getCD())
        newDamage = damage.calculate()

        self.character.setArtifact(artifactType, oldArtifact)


        if newDamage <= oldDamage:
            
            return False
        else:
            return True

    def RemoveSubstat(self, stat, statlist):
        # Given the name of the stat and the stalist: 

        # Remove a stat completely from the statlist
        statcount=statlist.count(stat)
        for i in range(statcount):
            statlist.remove(stat)
        return statlist

    def ChooseNumberStat(self, Substatname, index):
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
                return HPList[index]
            elif (Substatname == "PHP"):
                return PHPList[index]
            elif (Substatname == "DEF"):
                return DEFList[index]
            elif (Substatname == "PDEF"):
                return PDEFList[index]
            elif (Substatname == "ATK"):
                return ATKList[index]
            elif (Substatname == "PATK"):
                return PATKList[index]
            elif (Substatname == "EM"):
                return EMList[index]
            elif (Substatname == "ER"):
                return ERList[index]
            elif (Substatname == "CR"):
                return CRList[index]
            elif (Substatname == "CD"):
                return CDList[index]
            return -1

    def getMainStatNumber(self, statname, level):
            # Given the stat name and level of Artifact

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