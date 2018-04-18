from itertools import *
values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
#lambda function creates a small anonymous funcction/throw-away functions
for i in starmap(lambda x, y:(x, y, x * y), values):
    print('{} * {} = {}'.format(*i))
