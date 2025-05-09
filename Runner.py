
from Character import Character
from Substat import Substat
from Artifact import Artifact



a1 = Artifact("HP",4780, Substat("CD", 26.4), Substat("CR", 7.4), Substat("PATK", 0.105), Substat("ATK",16))
a2 = Artifact("ATK",311, Substat("ER", 5.8), Substat("CR", 7.0), Substat("EM", 79),  Substat("CD", 13.2))
a3 = Artifact("EM", 187,  Substat("PDEF", 0.058),  Substat("CR", 8.6),  Substat("PHP", 0.041),  Substat("CD", 24.9))
a4 = Artifact("CDMG", 0.466,  Substat("HP", 209),  Substat("ATK", 29),  Substat("EM", 42),  Substat("CD", 27.2))
a5 = Artifact("CD", 62.2,  Substat("PATK", 0.105),  Substat("CR", 7.8),  Substat("ATK", 31),  Substat("EM", 42))

list = [
    a1,
    a2,
    a3,
    a4,
    a5]
ganyu = Character(9796.73, 334.85, 630.21, list)

print(ganyu.getTotalATK())