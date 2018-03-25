class Godzilla():

    def __init__(self, stomach_vol):
        self.stomach_vol = stomach_vol
        self.stomach_remaining_space = stomach_vol
        self.stomach_full = False

    def eat(self, humans_weight):
        self.stomach_remaining_space -= humans_weight
        return self.stomach_remaining_space

    def is_full(self):
        if self.stomach_remaining_space <= self.stomach_vol * 0.1:
            self.stomach_full = True
            return True
        else:
            return False

Kesha = Godzilla(100)
print(Kesha.eat(90))
print(Kesha.is_full())

