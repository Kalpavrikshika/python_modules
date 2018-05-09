import numpy as numpy
x = numpy.arange(9).reshape(1,3,3)

print ('Array X:')
print (x)
print ('\n')
y = numpy.squeeze(x)

print('Array Y:')
print(y)
print('\n')

print('The shapes of X and Y array:')
print(x.shape, y.shape)
