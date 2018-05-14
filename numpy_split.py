import numpy as numpy
a = numpy.arange(9)

print ('First array')
print (a)
print ('\n')

print('Split the array')
b = numpy.split(a,3)
print(b)
print('\n')

print('Split the array')
b = numpy.split(a,[4,7])
print(b)