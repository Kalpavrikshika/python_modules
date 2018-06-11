from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print('I am doing boring work beofre executing a_func()')
        a_func()
        print('I am doing some boring work after executing a_func()')

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print('I am the function which needs some decoration to remove my foul smell')

print(a_function_requiring_decoration.__name__)
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
print(a_function_requiring_decoration())
