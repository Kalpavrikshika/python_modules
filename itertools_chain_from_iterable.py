from itertools import *

def make_iterables_to_chain():
    #yield is keyword for generator (Generator is not a list-collection.)
    yield [1,2,3]
    yield ['a', 'b', 'c']

for i in chain.from_iterable(make_iterables_to_chain()):
    print (i, end = ' ')
print()