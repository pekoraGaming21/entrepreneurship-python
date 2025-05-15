from RandomArtifact import RandomArtifact
from Character import Character
from Calculator import Calculator


class BetterArtifacts:
    

    def __init__(self, character):
        print("Better Artifacts on")
        self.character = character

        
    def randomize(self, type):

        oldArtifact = self.character.getArtifact(type)
        numOfArtifactsWorse = 0

        damage = Calculator()
        damage.setBase(self.character.getTotalATK() * 2.805, 1, 0)
        damage.setBonus(1.586)
        damage.setTarget(103, 90, 0.1, 0)
        damage.setAmp(self.character.getEM(), "Reverse Melt", 0)
        damage.setCritDMG("Average", self.character.getCR(), self.character.getCD())
        oldDamage = damage.calculate()

        sampledArtifacts = 100
        
        for i in range(sampledArtifacts):

            newArtifact = RandomArtifact(type)

            self.character.setArtifact(type, newArtifact)

            # print("Ganyu HP: " + str(self.character.getTotalHP()))
            print("Ganyu ATK: " + str(self.character.getTotalATK()))
            # print("Ganyu DEF: " + str(self.character.getTotalDEF()))
            print("Ganyu EM: " + str(self.character.getEM()))
            # print("Ganyu ER: " + str(self.character.getER()))
            print("Ganyu CR: " + str(self.character.getCR()))
            print("Ganyu CD: " + str(self.character.getCD()))


            damage.setBase(self.character.getTotalATK() * 2.805, 1, 0)
            damage.setBonus(1.586)
            damage.setTarget(103, 90, 0.1, 0)
            damage.setAmp(self.character.getEM(), "Reverse Melt", 0)
            damage.setCritDMG("Average", self.character.getCR(), self.character.getCD())
            newDamage = damage.calculate()

            print("New damage", newDamage)
            print("Old Damage", oldDamage)
            if newDamage <= oldDamage:
                numOfArtifactsWorse += 1
                print("increment worse artifacts")

            
        self.character.setArtifact(type, oldArtifact)

        # Proportions of artifacts worse
        return (numOfArtifactsWorse / sampledArtifacts) 
            
        

    

    # Make an artifact
    # Calculate damage with new artifact (and others constant)
    # If this new artifact damage is better, keep track)
    # FInd proportion of artifacts better

