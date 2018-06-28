class Cal(object):
    #pi is a class variable
    pi = 3.142
    def __init__(self, radius):
        #self.radius is an instance variable
        self.radius = radius
    def area(self):
        return self.pi * (self.radius ** 2)
a = Cal(32)
print(a.area())
#Output: 3217.408
print(a.pi)
#Output: 3.142
a.pi = 43
print(a.pi)
# Output: 43

b = Cal(44)
print(b.area())
#Output: 6082.912
print(b.pi)#Output : 3.142
b.pi = 50
print(b.pi)
#Output: 50
