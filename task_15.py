import math

def circles_intersect(x1, y1, r1, x2, y2, r2):
    dist = math.hypot(x2 - x1, y2 - y1)
    if dist > r1 + r2 or dist < abs(r1-r2): #случай когда два круга располагаются отдельно друг от друга или один в другом
        return False
    #случай касательной
    # elif dist == r1 + r2 or (r1 + r2) % 3 == 0:
    #     return True
    else:
        return True

print(circles_intersect(2, -2, 2, 1, 2, 2))
