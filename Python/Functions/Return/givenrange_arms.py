def start():
    upper = read('Enter the upper limit:')
    lower = read('Enter the lower limit:')
    display(upper, lower)

def display(upper, lower):                              
    for num in range(lower, upper):
        if is_armstrong(num) is True:
            print(num)

def is_armstrong(num):
    if num == armstrong_op(num):
        return True
    return False

def armstrong_op(num):
    count = count_of_digits(num)
    res = 0
    while num:
        last_digit = num % 10
        res = add(res, pow(last_digit, count))
        num = remove_last(num)
    return res

def count_of_digits(num):
    count = 0
    while num:
        count += 1
        num = remove_last(num)
    return count

def remove_last(num):
    return num // 10

def add(num1, num2):
    return num1 +num2

def read(msg):
    return int(input(msg))

start()