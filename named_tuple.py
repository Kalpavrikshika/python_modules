from collections import namedtuple

def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name = "Danny", age = 31)

p = profile()
print(p, type(p))

print(p.name)
print(p.age)

p = profile()
print(p[0])
print(p[1])

name, age = profile()
print(name)
print(age)