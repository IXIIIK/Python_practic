def fizz_buzz(begin, end):
    b = ''
    if begin > end:
        return ''

    for i in range(begin, end + 1):

        if i % 3 == 0 and i % 5 == 0:
            b += 'FizzBuzz '
        elif i % 3 == 0:
            b += 'Fizz '
        elif i % 5 == 0:
            b += 'Buzz ' 
        else:
            b += f'{str(i)} '
        
    return b.strip()


