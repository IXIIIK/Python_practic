def call_twice(arg, *args, **kwargs):

    a = arg(*args, **kwargs), arg(*args, **kwargs)
    return a



