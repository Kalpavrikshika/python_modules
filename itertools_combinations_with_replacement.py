from itertools import *

'''each input item is paired with itself as well as other 
members'''

def show(iterable):
    first = None
    for i , item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item))
    print()

print('Unique pairs:\n')
show(combinations_with_replacement('abcd' , r=2))