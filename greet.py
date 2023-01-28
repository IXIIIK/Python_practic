def greet(name, *args):
    res = (name, ) + args
    res = ' and '.join(res)

    return f'Hello, {res}!'



print(greet(*'ABC'))



