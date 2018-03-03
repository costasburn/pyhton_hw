def degrees2radians(degrees):
    ratio = 0.0174533
    radians = float(degrees) * ratio
    return radians

degrees = input("Please input degrees to convert in radians: ")


print("{} degrees equal to {} radians".format(degrees, degrees2radians(degrees)))