def fib(argument):
    a = 0
    b = 1
    for __ in range(argument):
        
        a, b = b, a + b 
    return a



print(fib(3))