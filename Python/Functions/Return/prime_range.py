def start():
    upper_limit = 50
    display(upper_limit)

def display(upper_limit):
    num = 2
    while upper_limit:
        if is_prime(num) is True:
            print(num)
            upper_limit = add(upper_limit, -1)
        num = add(num, 1)

def is_prime(num):
    if count_of_factor(num) == 2:
        return True
    return False

def count_of_factor(num):
    count = 0
    for var in range(1, num +1):
        if num % var == 0:
            count = add(count, 1)
    return count

def add(num1,num2):
    return num1 + num2

start()