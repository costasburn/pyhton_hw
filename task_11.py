import math

def degrees2radians(degrees):
    ratio = math.pi / 180
    radians = float(degrees) * ratio
    return radians

degrees = input("Please input degrees to convert in radians: ")


print("{} degrees equal to {} radians".format(degrees, degrees2radians(degrees)))