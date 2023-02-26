from functools import wraps

def memoizing(argument):
    def real_decorator(function):
        memory = {}
        @wraps(function)
        def inner(arg):
            memoized_result = memory.get(arg)
            if memoized_result is None:
                memoized_result = function(arg)
                memory[arg] = memoized_result
            elif len(memory) >= argument:
                memory.pop(arg)
            return memoized_result
        return inner
    return real_decorator


@memoizing(3)
def f(x):
    '''return bar'''
    print('Calculating...')
    return x * 10




