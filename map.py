#below is a no map technique
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print (squared)

#map
items = [1, 2, 3, 4, 5]
squared_1 = list(map(lambda x: x**2, items))
print (squared_1)