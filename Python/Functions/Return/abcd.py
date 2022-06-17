def start():
    num = operation()
    display(num)

def operation():
    num = 0
    for var in range(1000,10000):
        if var * 4 == reverse(var):
            num = var
            break
    return num

def display(num):
    d = last_digit(num)
    num = remove_last_digit(num)
    c = last_digit(num)
    num = remove_last_digit(num)
    b = last_digit(num)
    num = remove_last_digit(num)
    a = last_digit(num)
    num = remove_last_digit(num)
    print(f'abcd * 4 = dcba -> {a=}, {b=}, {c=}, {d=}')

def reverse(num):
    res = int()
    while num:
        last = last_digit(num)
        res = res  * 10 + last
        num = remove_last_digit(num)
    return res

def last_digit(num):
    return num % 10

def remove_last_digit(num):
    return num // 10

start()