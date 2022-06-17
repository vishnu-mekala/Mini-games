def start():
    upper = read('Enter the upper limit')
    lower = read('Enter the lower limit')
    display(upper, lower)

def display(upper, lower):                              
    for num in range(lower, upper):
        if is_prime(num) is True:
            print(num)

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

def read(msg):
    return int(input(msg))

start()