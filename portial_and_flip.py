def greet(name, surname):
    return f'Hello, {name} {surname}'

def partial_apply(function, name):
    def inner(i):
        return function(name, i)
    return inner

def flip(function):
    def inner(name, surname):
        return function(surname, name)    
    return inner
