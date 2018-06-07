#No set implementation
some_list = ['a', 'b', 'c', 'd', 'm', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

#With set implementation

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)