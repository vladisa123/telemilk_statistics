def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def mul(a,b):
    return a*b

def squares ():
    squares = [e*e for e in range(10) if e%2 == 0] # listcomps
    return squares


if __name__ == '__main__':
    # print(plus(1, 2))
    # print(minus(1, 2))
    # print(mul(1, 2))
    print(squares())
