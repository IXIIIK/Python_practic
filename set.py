def all_unique(arg):   
    b = []
    
    for i, d in enumerate(arg):
        b.append(d)

    if len(set(b)) == len(b):
        return True
    else:
        return False

    

print(all_unique(iter([1, 3, 4])))


