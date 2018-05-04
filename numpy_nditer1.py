import numpy as numpy
a = numpy.arange(0,60,5)
a = a.reshape(3,4)

print ('Original array is:')
print (a)
print ('\n')

print ('Transpose of original array is:')
b = a.T
print (b)
print ('\n')

print ('Modified array is:')
for x in numpy.nditer(b):
    print (x)