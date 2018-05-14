import numpy as numpy
a = numpy.arange(16).reshape(4,4)
print ('First array')
print(a)
print('\n')

print('Horizontal splitting')
b = numpy.hsplit(a,2)
print(b)
print('\n')