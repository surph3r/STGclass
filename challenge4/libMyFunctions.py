from num2words import num2words

def fibonacci_sequence(num):
    a,b = 1,1
    for i in range(num-1):
        a,b = b,a+b

    return a
