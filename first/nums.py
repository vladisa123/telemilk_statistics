def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def mul(a,b):
    return a*b

def squares ():
    squares = [e*e for e in range(10) if e%2 == 0] # listcomps

    text = 'hello world'
    words = [word.capitalize() for word in text.split()]

    ints = [1,4,2,-12]
    positives = [num for num in ints if num > 0]

    return squares, words, positives


if __name__ == '__main__':
    # print(plus(1, 2))
    # print(minus(1, 2))
    # print(mul(1, 2))
    print(squares())
