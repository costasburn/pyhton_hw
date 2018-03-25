import math


class circle():

    def __init__(self, rad, centr_x, centr_y):
        self.centr_x = centr_x
        self.centr_y = centr_y
        self.rad = rad

    def is_inside(self, point):
        dist = math.hypot(point.x - self.centr_x, point.y - self.centr_y)
        if dist < self.rad:
            return True
        else:
            return False


class point():

    def __init__(self, x, y):
        self.x = x
        self.y = y


my_circle = circle(5, 1, 2)
my_point = point(6, 2)
print(my_circle.is_inside(my_point))

