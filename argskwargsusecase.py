def test_args_kwargs(args1, args2, args3, args4, **kwargs):
    print('Args1', args1)
    print('Args2', args2)
    print('Args3', args3)
    print('Args4', args4)

    for item, value in kwargs.items():
        print("{0} : {1}".format(item, value))

args = ('Bob', 'Lolo', 'Stacy', 'Len')
test_args_kwargs(*args)
    
test_args_kwargs(*args, firstname = 'Bob', secondname ='Lolo', thirdname ='Stacy', fourthname = 'Len')

