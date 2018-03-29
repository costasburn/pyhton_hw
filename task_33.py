class Godzilla:
    STOMACH_VOL = 100
    STOMACH_FILL_LIMIT = STOMACH_VOL * 0.1

    def __init__(self):
        self.stomach_remaining_space = self.STOMACH_VOL

    def eat(self, humans_weight):
        if self.is_full():
            print("Already full")
        elif humans_weight >= self.stomach_remaining_space:
            print("Human is too heavy")
        else:
            self.stomach_remaining_space -= humans_weight
        return self.stomach_remaining_space

    def is_full(self):
        return self.stomach_remaining_space <= self.STOMACH_FILL_LIMIT


Kesha = Godzilla()
print(Kesha.eat(50))
print(Kesha.eat(45))
print(Kesha.eat(1))
print(Kesha.is_full())
