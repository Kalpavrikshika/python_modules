from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name = "Perry", age = 31, type = "cat")
print(perry._asdict())
