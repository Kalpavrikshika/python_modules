from itertools import *

def show(iterable):
    first = None
    for i, item in enumerate(iterable , 1):
        if first != item[0]:
            if first is not None:
                #print first character
                print()
            first = item[0]
            #printing second character
        print('#'.join(item), end = ' ')

    #print()

print('Unique pairs:\n')
show(combinations('abcd', r=2))