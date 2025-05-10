class Calculator:
    def __init__(self):
        print("Calculator on")
        self.baseDMG = 0
        self.baseMult = 0
        self.baseAddDMG = 0
        self.bonusDMGMult = 0
        self.targetDefMult = 0
        self.targetResMult = 0
        self.critDMG = 0
        self.ampMult = 0

    def setBase(self, dmg, mult, add):
        self.baseDMG = dmg
        self.baseMult = mult
        self.baseAddDMG = add

    def setBonus(self, bonus):
        self.bonusDMGMult = bonus

    def setTarget(self, enemyLvl, charLvl, enemyres, resShred):
        self.targetDefMult = (charLvl + 100) / (1 * (enemyLvl + 100) + (charLvl + 100))
        

        self.targetResMult = enemyres
        temp = resShred

        
        if self.targetResMult > 0.75 and self.targetResMult - resShred < 0.75:
            # NOT RIGHT
            self.targetResMult = 1 / (4 * enemyres + 1)
        
        # 
        elif self.targetResMult > 0.75:
            self.targetResMult = 1 / (4 * enemyres + 1)

        elif self.targetResMult > 0 and self.targetResMult - resShred < 0:
            temp = resShred - enemyres
            self.targetResMult = 1 - (-temp/2)

        #
        elif self.targetResMult > 0:
            self.targetResMult = 1 - enemyres

        elif self.targetResMult < 0:
            self.targetResMult = 1 - (enemyres / 2)
        print("Target res Multi: " + str(self.targetResMult))
        print("Target Def Multi: " + str(self.targetDefMult))
       

    def setAmp(self, em, reaction, reactionBonus = 0):
        if reaction == "Reverse Melt" or reaction == "Reverse Vaporize":
            self.ampMult = 1.5 * (1 + 2.78 * (em / (em + 1400)) + reactionBonus)
            print("Reverse reaction")
        elif reaction == "Forward Melt" or reaction == "Forward Vaporize":
            self.ampMult = 2 * (1 + 2.78 * (em / (em + 1400)) + reactionBonus)
            print("Forward reaction")
        else:
            self.ampMult = 1


        # self.ampMult = inn

    def setCritDMG(self, crit):
        self.critDMG = crit

    def calculate(self):
        print(((self.baseDMG * self.baseMult) + self.baseAddDMG)* self.bonusDMGMult * self.targetDefMult * self.targetResMult * self.ampMult)