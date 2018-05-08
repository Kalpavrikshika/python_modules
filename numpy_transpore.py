import numpy as numpy
a = numpy.arange(12).reshape(3,4)

print('The original array is:')
print(a)
print('\n')

print('The transposed array is:')
b = numpy.transpose(a)
print(b)