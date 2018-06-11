def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
#output:0
print(next(gen))
#output:1
print(next(gen))
#output:2
print(next(gen))
