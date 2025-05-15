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
        coolerArtifacts = []

        damage = Calculator()
        damage.setBase(self.character.getTotalATK() * 1.50, 1, 0)
        damage.setBonus(0, self.character.getElement(), "Anemo", self.character.getElementalDMG("Anemo"))
        damage.setTarget(103, 90, 0.1, 0)
        damage.setAmp(self.character.getEM(), "None", 0)
        damage.setCritDMG("Average", self.character.getCR(), self.character.getCD())
        oldDamage = damage.calculate()

        sampledArtifacts = 10000
        
        for i in range(sampledArtifacts):
            if i % 1000 == 0:
                print("Artifact #" + str(i))

            newArtifact = RandomArtifact(type)

            self.character.setArtifact(type, newArtifact)

            # print("Ganyu HP: " + str(self.character.getTotalHP()))
            # print("Ganyu ATK: " + str(self.character.getTotalATK()))
            # print("Ganyu DEF: " + str(self.character.getTotalDEF()))
            # print("Ganyu EM: " + str(self.character.getEM()))
            # print("Ganyu ER: " + str(self.character.getER()))
            # print("Ganyu CR: " + str(self.character.getCR()))
            # print("Ganyu CD: " + str(self.character.getCD()))


            damage.setBase(self.character.getTotalATK() * 1.50, 1, 0)
            damage.setBonus(0, self.character.getElement(), "Anemo", self.character.getElementalDMG("Anemo"))
            damage.setTarget(103, 90, 0.1, 0)
            damage.setAmp(self.character.getEM(), "None", 0)
            damage.setCritDMG("Average", self.character.getCR(), self.character.getCD())
            newDamage = damage.calculate()

            if newDamage <= oldDamage:
                # if newDamage > 3970:
                #     print(newArtifact)
                #     print("New Damage:", str(newDamage))
                #     print("Old Damage:", str(oldDamage))

                numOfArtifactsWorse += 1
            else:
                coolerArtifacts.append(newArtifact)

            
        self.character.setArtifact(type, oldArtifact)

        print("Number of artifacts better: " + str(sampledArtifacts - numOfArtifactsWorse))
        print("Cooler artifacts:")
        for artifact in coolerArtifacts:
            print(artifact)
        # Proportions of artifacts worse
        return (numOfArtifactsWorse / sampledArtifacts) 
            
        

    

    # Make an artifact
    # Calculate damage with new artifact (and others constant)
    # If this new artifact damage is better, keep track)
    # FInd proportion of artifacts better

