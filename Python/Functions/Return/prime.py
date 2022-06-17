def is_prime(num):
    if count_of_factor(num) == 2:
        print(f'{num} is a Prime Number')
    else:
        print(f'{num} is not a Prime Number')

def count_of_factor(num):
    count = 0
    for div in range(1, num+1):
        if divisible(num, div) is True:
            count = add(count, 1)
    return count

def divisible(divd, div):
    return divd % div == 0
def add(num1,num2):
    return num1 + num2
num = int(input('Enter a number:'))
is_prime(num)

def my_func(fname):
    print(fname + ' ' 'Vardhan')
my_func('Vishnu')

def my_func(x):
    return 5 * x
print(my_func(5))