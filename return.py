def add (value1, value2):
    global result
    result = value1 + value2

add(2, 4)
result
print(result)

def profile():
    global name
    global age
    name = "Danny"
    age = 30

profile()
print(name)
print(age)