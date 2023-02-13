def a(func):
    def inner(args, **kwargs):
        func(args, **kwargs)
        res = func(args)
        return res
    return inner

def call_twice(arg, *args, **kwargs):

    a = arg(*args, **kwargs), arg(*args, **kwargs)
    return a

print(call_twice(input, 'enter: '))


