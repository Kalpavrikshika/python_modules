import numpy as numpy
a = numpy.arange(4).reshape(1,4)

print('The original array:')
print(a)
print('\n')

print('After applying the broadcast to function:')
print(numpy.broadcast_to(a,(4,4)))
print('\n')
