from Character import Character
from Substat import Substat
from Artifact import Artifact
from Calculator import Calculator
from RandomArtifact import RandomArtifact
from BetterArtifacts import BetterArtifacts
from NewArtifactProbability import NewArtifactProbability


# a1 = Artifact("Flower", "HP",4780, Substat("CR", 10.1), Substat("CD", 21.8), Substat("EM", 40), Substat("PHP",0.058))
# a2 = Artifact("Feather", "ATK",311, Substat("CD", 14.0), Substat("CR", 9.7), Substat("ER", 5.2),  Substat("EM", 65))
# a3 = Artifact("Sands", "EM", 187,  Substat("ATK", 16),  Substat("HP", 209),  Substat("CD", 21.8),  Substat("PATK", 0.163))
# a4 = Artifact("Goblet", "CDMG", 0.466,  Substat("HP", 209),  Substat("ATK", 29),  Substat("EM", 42),  Substat("CD", 27.2))
# a5 = Artifact("Circlet", "CD", 62.2,  Substat("ATK", 14),  Substat("PHP", 0.058),  Substat("EM", 82),  Substat("CR", 9.7))

# a1 = RandomArtifact("Flower")
# a2 = RandomArtifact("Feather")
# a3 = RandomArtifact("Sands")
# a4 = RandomArtifact("Goblet")
# a5 = RandomArtifact("Circlet")

# COURTNEY WANDERER ARTIFACTS

a1 = Artifact("Flower", "HP", 4780, Substat("ATK", 16), Substat("CR", 14.8), Substat("ER", 10.5 ), Substat("CD", 17.1))
a2 = Artifact("Feather", "ATK", 311, Substat("CD", 32.6), Substat("CR", 2.7), Substat("HP", 239),  Substat("PATK", 0.041))
a3 = Artifact("Sands", "PATK", 0.466,  Substat("CR", 3.1),  Substat("CD", 36.5),  Substat("ER", 5.2),  Substat("ATK", 16))
a4 = Artifact("Goblet", "ADMG", 0.466,  Substat("CR", 7.4),  Substat("CD", 23.3),  Substat("ER", 10.4),  Substat("PATK", 0.117))
a5 = Artifact("Circlet", "CD", 62.2,  Substat("EM", 63),  Substat("ATK", 14),  Substat("CR", 13.2),  Substat("PDEF", 0.066))

list = [a1,a2,a3,a4,a5]
    
# extraStats = [["ATK", 1377.686], ["CR", 66.1]]
extraStats = []

# ganyu = Character("Cryo", 90, 9796.73, 334.85, 630.21, "Hunter's Path", 541.83, list, "CD", 38.4, extraStats)
wanderer = Character("Anemo", 90, 10164.11, 327.67, 607.16, "The Widsith", 510, list, "CR", 19.2, extraStats)


# print("Ganyu HP: " + str(ganyu.getTotalHP()))
# print("Ganyu ATK: " + str(ganyu.getTotalATK()))
# print("Ganyu DEF: " + str(ganyu.getTotalDEF()))
# print("Ganyu EM: " + str(ganyu.getEM()))
# print("Ganyu ER: " + str(ganyu.getER()))
# print("Ganyu CR: " + str(ganyu.getCR()))
# print("Ganyu CD: " + str(ganyu.getCD()))


# damage = Calculator()
# damage.setBase(ganyu.getTotalATK() * 2.805, 1, 0)
# damage.setBonus(0.12, ganyu.getElement(), "Cryo", ganyu.getElementalDMG("Cryo"))
# damage.setTarget(103, 90, 0.1, 0)
# damage.setAmp(ganyu.getEM(), "ReverseMelt", 0)
# damage.setCritDMG("Average", ganyu.getCR(), ganyu.getCD())
# print(damage.calculate())

# test = BetterArtifacts(wanderer)
# print("Probability of artifacts worse:", str(test.randomize("Circlet")))

# Ganyu ATK with bennett burst (and noblessed): 2768
testArtifact = Artifact("Flower", "HP", 4780, Substat("PATK", 0.041), Substat("CR", 3.9), Substat("ER", 4.5), Substat("CD", 7.8))
test2 = NewArtifactProbability(testArtifact, wanderer, 0)
print(test2.Probability())