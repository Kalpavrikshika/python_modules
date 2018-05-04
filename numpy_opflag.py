import numpy as numpy
a = numpy.arange(0,60,5)
a = a.reshape(3,4)
print ('Original array is:')
print (a)
print ('\n')

for x in numpy.nditer(a, op_flags=['readwrite']):
    x[...]=2*x
print ('Modified array is:')
print (a)