import numpy as numpy
a = numpy.array([5,2,6,2,7,5,6,8,2,9])

print ('First array:')
print(a)
print('\n')

print('Unique values of first array:')
u = numpy.unique(a)
print(u)
print('\n')

print('Unique array and indices array:')
u, indices = numpy.unique(a, return_index = True)
print (indices)
print('\n')

print('We can see each number corresponds to index in original array:')
print(a)
print('\n')

print('Indices of unique array:')
u, indices = numpy.unique(a, return_inverse = True)
print (u)
print ('\n')

print('Indices are:')
print(indices)
print('\n')

print('Reconstruct the original array using indices')
print (u[indices])
print ('\n')

print('Return the count repetitions of unique elements:')
u, indices = numpy.unique(a, return_counts = True)
print(u)
print(indices)