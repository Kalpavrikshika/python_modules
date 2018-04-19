'''cycle function returns an iterator 
that repeats the arguments. 
comsumes quite a bit of memory.'''

from itertools import *

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)