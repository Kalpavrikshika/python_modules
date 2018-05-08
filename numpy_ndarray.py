#same functionality as a transpose
import numpy as numpy
a = numpy.arange(12).reshape(3,4)

print ('The original array is:')
print (a)
print ('\n')

print('Array after applying the function')
print (a.T)