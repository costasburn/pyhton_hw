import math

def triangle_square_and_perimeter(a, b):
    area = 0.5 * a * b
    hypotenuse = math.sqrt(a**2 + b**2)
    perimetr = a + b + hypotenuse
    return area, perimetr


a = 3
b = 4

area, perimetr = triangle_square_and_perimeter(a, b)


print("Площадь прямоугольного триугольника с катетами {} и {} равняется {}. А его периметр - {}".format(a, b, area, perimetr))
