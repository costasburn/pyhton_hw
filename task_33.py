import random

class Godzilla(object):

    def __init__(self, stomach_vol):
        self.stomach_vol = stomach_vol
        self.stomach_full = False

    def eat_people(self):
        while self.stomach_vol > 10:
            victims_weight = random.randint(0, self.stomach_vol)
            self.stomach_vol -= victims_weight
            print("Kesha has eaten 1 man, remaining stomach vol: {}".format(self.stomach_vol))
        print("Kesha is not hungry anymore")


Kesha = Godzilla(100)
print(Kesha.eat_people())

