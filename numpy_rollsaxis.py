import numpy as numpy

a = numpy.arange(8).reshape(2,2,2)
print ('The original array:')
print (a)
print ('\n')

print ('After applying rollaxis function:')
print (numpy.rollaxis(a,2))
print ('\n')

print('After applying rollaxis funtion:')
print(numpy.rollaxis(a,2,1))