from itertools import *
#The chain function takes several iterators as arguments and returns a single iterator.
#A chain makes it easy to process several sequences withoutco
#constructing one large list.
for i in chain ([1,2,3], ['a', 'b', 'c']):
    print (i, end = ' ')
print ()