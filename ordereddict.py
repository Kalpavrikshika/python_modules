from collections import OrderedDict
# problem 

colours = {"red" : 198, "Green": 170, "Blue": 160}
for key, value in colours.items():
    print(key, value)

#solution
colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)
