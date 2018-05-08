import numpy as numpy
a = numpy.arange(8).reshape(2,4)

print('The original array is:')
print (a)
print ('\n')

print('The flattened array is:')
print(a.flatten())
print('\n')

print('The flattened array in F-style')
print(a.flatten(order = 'F'))