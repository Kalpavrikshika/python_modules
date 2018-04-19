'''the repeat funtion returns the iterator that 
produces the same value each time it's accessed.'''


from itertools import *

for i in repeat('over-and-over', 5):
    print(i)