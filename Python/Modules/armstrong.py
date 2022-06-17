import common

def is_armstrong(num):
    if common.is_equal(armstrong_op(num), num):
        print(f'{num} is an Armstrong Number')
    else:
        print(f'{num} is not an Armstrong Number')

def armstrong_op(num):
    digit_count = count_no_of_digit(num)
    res = 0
    while num:
        last_digit = common.divisible(num, 10)
        res += (last_digit ** digit_count)
        num = common.remove_last_digit(num, 10)
    return res

def count_no_of_digit(num):
    count = 0
    while num:
        num = common.remove_last_digit(num, 10)
        count += 1
    return count