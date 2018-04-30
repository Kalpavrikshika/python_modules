from itertools import *

def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end = ' ')
    print()

print('All permutations: \n')
show(permutations('abcd'))

print('\nPairs:\n')
#use r argument to limit the length and number of the individual permutations.
show(permutations('abcd' , r = 2))
