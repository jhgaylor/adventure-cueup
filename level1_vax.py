class Vex(object):

    def __init__(self, seed):
        self.a = 69069
        self.m = (2**32)
        self.c = 1
        self.seed = seed
        #print self.m

    def get(self):

        self.seed = ((self.a*self.seed)+self.c) % self.m
        return self.seed

v = Vex(6)

pattern = []
while(True):
    val = v.get()
    if val%36 in pattern:
        break
    pattern.append(val%36)
        
print pattern
