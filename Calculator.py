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

        if self.targetResMult >= 0.75 and self.targetResMult - resShred < 0.75:
            # NOT RIGHT
            self.targetResMult = 1 / (4 * enemyres + 1)
        
        elif self.targetResMult >= 0.75:
            self.targetResMult = 1 / (4 * enemyres + 1)

        elif self.targetResMult >= 0 and self.targetResMult - resShred < 0:
            temp = resShred - enemyres
            self.targetResMult = 1 - (-temp/2)

        elif self.targetResMult >= 0:
            self.targetResMult = 1 - enemyres

        elif self.targetResMult < 0:
            self.targetResMult = 1 - (enemyres / 2)

    def setAmp(self, em, reaction, reactionBonus = 0):
        if reaction == "Reverse Melt" or reaction == "Reverse Vaporize":
            self.ampMult = 1.5 * (1 + 2.78 * (em / (em + 1400)) + reactionBonus)
            # print("Reverse reaction")
        elif reaction == "Forward Melt" or reaction == "Forward Vaporize":
            self.ampMult = 2 * (1 + 2.78 * (em / (em + 1400)) + reactionBonus)
            # print("Forward reaction")
        else:
            self.ampMult = 1

    def setCritDMG(self, critical, CR, CD):
        self.hit = critical
        self.critRate = CR
        if CR > 100:
            self.critRate = 100
        self.critDMG = CD

    def calculate(self):
        NonCrit = ((self.baseDMG * self.baseMult) + self.baseAddDMG) * self.bonusDMGMult * self.targetDefMult * self.targetResMult * self.ampMult
        if self.hit == "NonCrit":
            print(NonCrit)
        elif self.hit == "Average":
            print((self.critRate / 100) * (1 + (self.critDMG / 100)) * NonCrit + ((100 - self.critRate) / 100) * NonCrit)
        elif self.hit == "Crit":
            print(NonCrit * (1 + self.critDMG / 100))