class Substat:
    def __init__(self, s="Wrong", v=0):
        self.stat = s
        self.value = v

    def getStat(self):
        return self.stat
    
    def getValue(self):
        return self.value
    
    def __str__(self):
        return f"{self.stat}: {self.value}"