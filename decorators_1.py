#Giving a function as an argument to another function
def hi():
    return ("hi yasoob!")

def doSomethingBeforeHi(func):
    print('I am doing some boring work before executing hi()')
    print(func())

doSomethingBeforeHi(hi)

