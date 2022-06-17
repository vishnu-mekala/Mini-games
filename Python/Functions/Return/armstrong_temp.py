def start():
    num = int(input('Enter the value:'))
    status = is_armstrong(num)
    display(num, status)

def is_armstrong(num):
    if num == armstrong_op(num):
        return True
    return False

def armstrong_op(num):
    count = count_of_digits(num)
    res = 0
    while num:
        last_digit = num % 10
        res += pow(last_digit, count)
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

def display(num, status):
    if status is True:
        print(f'{num} is an Armstrong Number')
    else:
        print(f'{num} is not an Armstrong Number')

start()
