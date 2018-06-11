from decorator_2 import a_new_decorator

@a_new_decorator
def a_function_requiring_decoration():
    print('I am the function which needs some decoration to remove my foul smell')

a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)