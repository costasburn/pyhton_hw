import math


def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1, x2 = (-b + math.sqrt(discriminant)) / (2 * a), (-b - math.sqrt(discriminant)) / (2 * a)
    elif discriminant == 0:
        x1, x2 = (-b + math.sqrt(discriminant))
        return x1
    else:
        x1, x2 = None, None
    return x1, x2


print(solve_quadratic_equation(1, -8, 12))
