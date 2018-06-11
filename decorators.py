#returning functions from within functions
def hi (name = "b"):
    def greet():
        return ("Now you're in the greet() function")

    def welcome():
        return ("Now you're in the welcome() function")

    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a)
print(a())