import numpy as numpy
a = numpy.array([[1,2],[3,4]])

print ('First array:')
print(a)
print('\n')

b = numpy.array([[5,6],[7,8]])

print('Second array:')
print(b)
print('\n')

print('Joining the two arrays along axis-0')
print(numpy.concatenate((a,b)))
print('\n')

print('Joining the two arrays along axis-1')
print(numpy.concatenate((a,b),axis = 1))