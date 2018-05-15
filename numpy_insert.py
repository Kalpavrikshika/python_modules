import numpy as numpy
a = numpy.array([[1,2], [3,4], [5,6]])

print ('First array:')
print(a)
print('\n')

print('Axis parameter not passed. The input array is flattened before insertion')
print(numpy.insert(a,3,[11,12]))
print('\n')

print('Axis parameter passed. the values array is broadcast to match input array')
print('Broadcast along axis 0:')
print(numpy.insert(a,1,[11],axis = 0))
print('\n')

print('Broadcast along axis 1:')
print(numpy.insert(a,1,11,axis = 1))