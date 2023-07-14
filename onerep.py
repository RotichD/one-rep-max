import math

class OneRep:
    def __init__(self, weight, reps, increments = 5):
        self.weight = weight
        self.reps = reps
        self.increments = increments

    def roundWeight(self, input):
        return self.increments * round(input/self.increments)

    def brzycki(self):
        return round(self.weight * (36/(37 - self.reps)))

    

    
benchPress = OneRep(165, 6)
brzycki = benchPress.brzycki()
