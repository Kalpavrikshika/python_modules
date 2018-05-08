import numpy as numpy
a = numpy.arange(8).reshape(2,4)
print ('The original array')
print (a)
print ('\n')

print ('After applying the flat function:')
print (a.flat[5])