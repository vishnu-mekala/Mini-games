import common

def is_prime(num):
    if common.is_equal(count_of_factors(num), 2):
        print(f'{num} is a Prime Number')
    else:
        print(f'{num} is not a Prime Number')

def count_of_factors(num):
    count = 0
    for n in range(1, num +1):
        if common.is_equal(common.divisible(num, n), 0):
            count += 1
    return count