import numpy as numpy
a = numpy.array([[1,2,3],[4,5,6]])

print ('First array:')
print(a)
print('\n')

print('Append elements to array:')
print (numpy.append(a, [7,8,9]))
print('\n')

print ('Append elements along axis 0:')
print (numpy.append(a,[[7,8,9]],axis = 0))
print('\n')

print('Append elements along axis 1:')
print (numpy.append(a, [[5,5,5], [7,8,9]], axis = 1))
