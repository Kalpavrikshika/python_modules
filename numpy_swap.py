import numpy as numpy
a = numpy.arange(8).reshape(2,2,2)

print ('The original array:')
print(a)
print('\n')

print('The array after applying the swapaxes function:')
print(numpy.swapaxes(a,2,0))