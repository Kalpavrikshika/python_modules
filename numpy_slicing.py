import numpy as numpy
a = numpy.array([(1,2,3,4) , (3,4,5,6)])
print (a)
#2 element of zeroth element
print(a[0,2])
#2nd element of zeroth and first indec
print(a[0: ,2])

b = numpy.array([(8,9), (10,11), (12,13)])
print(b)
print(b[0:2,1])