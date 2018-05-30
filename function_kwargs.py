def test_args_kwargs(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)

#first with *args
args = ("two", 3, 5)
test_args_kwargs(*args)

#now with **kwargs
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
