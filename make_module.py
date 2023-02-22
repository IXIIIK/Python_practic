def make_module(step=1):
    return {'inc': lambda x: x + step, 'dec': lambda x: x - step}

m = make_module()

print(m['dec'](19))


