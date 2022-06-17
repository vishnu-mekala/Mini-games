def start():
    upper = read('Enter the upper limit:')
    lower = read('Enter the lower limit:')
    display(upper, lower)

def display(upper, lower):
    for num in range(lower, upper):
        if is_strong(num) is True:
            print(num)

def is_strong(num):
    if num == strong_op(num):
        return True
    return False

def strong_op(num):
    res = 0
    var =  1
    fact = 1
    last_digit = num % 10
    for var in range(1, last_digit+1):
        fact = fact * var
        var = var + 1
    res = res + fact
    num = num//10

def read(msg):
    return int(input(msg))

start()