import numpy as numpy
x = numpy.array([[1,2],[3,4]])

print('Array x:')
print(x)
print('\n')
y = numpy.expand_dims(x, axis = 0)

print('Array y:')
print(y)
print('\n')

print('The shape of X and Y array:')
print (x.shape, y.shape)
print('\n')
#insert axis at pos 1
y = numpy.expand_dims(x, axis=1)

print('Array Y after inserting axis at position 1')
print(y)
print('\n')

print('x.ndim and y.ndim:')
print(x.ndim, y.ndim)
print('\n')

print('x.shape and y.shape')
print(x.shape, y.shape)