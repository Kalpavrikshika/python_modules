import numpy as numpy
a = numpy.array([[1,2,3],[3,4,5],[4,5,6]])

print ('Our array is:')
print (a)
print ('\n')

print ('The items in the second column are:')
print (a[...,1])
print ('\n')

print ('The items in the second row are:')
print (a[1,...])
print ('\n')

print('The items column 1 onwards are:')
print (a[...,1:])