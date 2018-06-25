#list
squared = [x**2 for x in range(10)]
print(squared)

#dict
mcase = {'a': 10, 'b': 34, 'A':7, 'Z':3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

print(mcase)
