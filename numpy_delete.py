import numpy as numpy
a = numpy.arange(12).reshape(3,4)

print('First array')
print(a)
print('\n')

print('Array flattened before deleting operation')
print (numpy.delete(a,5))
print('\n')

print('Column 2 deleted')
print(numpy.delete(a,1,axis = 1))
print('\n')

print('A slice containing alternate values from array deleted:')
a = numpy.array([1,2,3,4,5,6,7,8,9,10])
print(numpy.delete(a, numpy.s_[::2]))