import math
var_a = 23
var_b = 42
var_c = 17
task1 = (var_a + var_b * (var_c / 2))
print("{} + {} * ({}/ 2)) = {}".format(var_a, var_b, var_c, task1))
task2 = ((var_a**2) + (var_b**2)) % 2
print("(({}^2) + ({}^2)) % 2 = {}".format(var_a, var_b, task2))
task3 = (var_a + var_b) / 12 * var_c % 4 + var_b
print("({0} + {1}) / 12 * {2} % 4 + {1} = {3}".format(var_a, var_b, var_c, task3))
task4 = (var_a - (var_b * var_c))/(var_a + var_b) % var_c
print("({0} - {1} * {2} ) / ( {0} + {1} ) % {2} = {3}".format(var_a, var_b, var_c, task4))
task5 = abs(var_a - var_b)/((var_a + var_b)**3) - math.cos(var_c)
print("|{0} - {1}| /( {0} + {1})^3 - cos( 2 ) = {3}".format(var_a, var_b, var_c, task5))
task6 = ((math.log1p(var_c) / (0 - var_b))**4) + abs(var_a)
print("(ln( 1 + {2} ) / (-{1}) )^4 + |{0}| = {3}".format(var_a, var_b, var_c, task6))