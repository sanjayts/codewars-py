
def square_digits(num):
    num_str = str(num)
    squares = [str(int(c)**2) for c in num_str]
    return int(''.join(squares))
