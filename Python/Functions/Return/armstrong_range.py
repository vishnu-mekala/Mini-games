def start():
    upper_limit = 15
    display(upper_limit)

def display(upper_limit):
    num = 1
    while upper_limit:
        if is_armstrong(num) is True:
            print(num)
            upper_limit = add(upper_limit, -1)
        num = add(num, 1)

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

start()