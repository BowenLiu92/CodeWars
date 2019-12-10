def square_digits(num):
    return int(''.join([str(int(e)**2) for e in list(str(num))]))