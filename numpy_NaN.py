import numpy as numpy
#Not a NUmber elements are omitted by using ~ 
a = numpy.array([numpy.nan, 1,2,numpy.nan,3,4,5])
print (a[~numpy.isnan(a)])