import numpy as numpy
a = numpy.array([[1,2],[3,4]])

print ('First array')
print (a)
print('\n')
b = numpy.array([[5,6],[7,8]])

print('Second array')
print(b)
print('\n')

print('Stack the two arrays along axis 0')
print(numpy.stack((a,b),0))
c = numpy.stack((a,b),0)
print(c.shape)
print('\n')

print('Stack the two arrays along the axis 1:')
print(numpy.stack((a,b),1))
d = numpy.stack((a,b),1)
print(d.shape)
print('\n')