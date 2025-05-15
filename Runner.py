from Character import Character
from Substat import Substat
from Artifact import Artifact
from Calculator import Calculator
from RandomArtifact import RandomArtifact


# a1 = Artifact("Flower", "HP",4780, Substat("CR", 10.1), Substat("CD", 21.8), Substat("EM", 40), Substat("PHP",0.058))
# a2 = Artifact("Feather", "ATK",311, Substat("CD", 14.0), Substat("CR", 9.7), Substat("ER", 5.2),  Substat("EM", 65))
# a3 = Artifact("Sands", "EM", 187,  Substat("ATK", 16),  Substat("HP", 209),  Substat("CD", 21.8),  Substat("PATK", 0.163))
# a4 = Artifact("Goblet", "CDMG", 0.466,  Substat("HP", 209),  Substat("ATK", 29),  Substat("EM", 42),  Substat("CD", 27.2))
# a5 = Artifact("Circlet", "CD", 62.2,  Substat("ATK", 14),  Substat("PHP", 0.058),  Substat("EM", 82),  Substat("CR", 9.7))

a1 = RandomArtifact("Flower")
a2 = RandomArtifact("Feather")
a3 = RandomArtifact("Sands")
a4 = RandomArtifact("Goblet")
a5 = RandomArtifact("Circlet")

list = [a1,a2,a3,a4,a5]

ganyu = Character("Cryo", 9796.73, 334.85, 630.21, "Hunter's Path", 541.83, list, "CD", 38.4)

print("Ganyu HP: " + str(ganyu.getTotalHP()))
print("Ganyu ATK: " + str(ganyu.getTotalATK()))
print("Ganyu DEF: " + str(ganyu.getTotalDEF()))
print("Ganyu EM: " + str(ganyu.getEM()))
print("Ganyu ER: " + str(ganyu.getER()))
print("Ganyu CR: " + str(ganyu.getCR()))
print("Ganyu CD: " + str(ganyu.getCD()))

damage = Calculator()
damage.setBase(ganyu.getTotalATK() * 2.805, 1, 0)
damage.setBonus(0, "Cryo", "Cryo", ganyu.getCDMG())
damage.setTarget(103, 90, 0.1, 0)
damage.setAmp(ganyu.getEM(), "None", 0)
damage.setCritDMG("NonCrit", ganyu.getCR(), ganyu.getCD())
damage.calculate()

test = RandomArtifact(None)
