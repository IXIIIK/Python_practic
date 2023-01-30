def updated(d, **kwargs):
 
    res = d.copy()
    res |= kwargs

    return res
    
    


d = {'a': 1, 'b': False}
print(updated(d, a=2, b=True, c=None))

print(updated(d) == d)

print(updated(d) is d)



