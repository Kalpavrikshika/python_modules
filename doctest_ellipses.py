class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.
    
    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
        [<doctest_ellipsis.MyClass obj at 0x...>]
        """
    return obj