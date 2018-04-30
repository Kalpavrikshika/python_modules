import numpy as numpy

x = numpy.array([(1,2,3),(3,4,5)])
y = numpy.array([(1,2,3),(3,4,5)])
print(numpy.vstack((x,y)))
print(numpy.hstack((x,y)))