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

    def setTarget(self, defe, res):
        self.targetDefMult = defe
        self.targetResMult = res

    def setAmp(self, inn):
        self.ampMult = inn

    def setCritDMG(self, crit):
        self.critDMG = crit

    def calculate(self):
        print(((self.baseDMG * self.baseMult) + self.baseAddDMG)* self.bonusDMGMult * self.targetDefMult * self.targetResMult * self.ampMult)