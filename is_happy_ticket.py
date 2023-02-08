def is_happy_ticket(ticket):
    result = list(map(int ,ticket))

    a = result[:len(result) // 2]
    b = result[len(result) // 2:]

    if sum(a) == sum(b):
        return True
    else: 
        return False
