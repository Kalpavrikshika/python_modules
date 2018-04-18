from itertools import *

Celsius = [39.2, 36.5, 37.3, 37.8]

#mapping lambda function (lambda x : expression)
Fahrenheit = list(map (lambda x : (float(9)/5) * x + 32, Celsius))
print (Fahrenheit)

c = list(map(lambda x: (float(5)/9)* (x-32), Fahrenheit))
print (c)