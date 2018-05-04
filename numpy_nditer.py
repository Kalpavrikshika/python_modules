import numpy as numpy
a = numpy.arange(0,60,5)
a = a.reshape(3,4)

print ('Original array is:')
print (a)
print ('\n')

print ('Modified array is:')
for x in numpy.nditer(a):
    print (x '\t')
