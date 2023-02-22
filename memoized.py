def memoized(function):
    memory = {}
    def inner(arg):
        if arg not in memory:
            result = function(arg)
            memory[arg] = result
            return result
        else:
            return memory.get(arg)
 
    return inner
   

@memoized
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))

print(f(1))