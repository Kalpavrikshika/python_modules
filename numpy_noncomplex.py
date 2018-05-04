import numpy as numpy

a = numpy.array([1, 2+6j, 5, 3.5+5j])

print (a[numpy.iscomplex(a)])