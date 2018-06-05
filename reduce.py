from functools import reduce
# without reduce tool
product = 1
list = [1, 2, 3, 4]

for num in list:
    product = product * num
print (product)

#with reduce tool
product = reduce((lambda x, y: x * y), [1,2,3,4])
print (product)
