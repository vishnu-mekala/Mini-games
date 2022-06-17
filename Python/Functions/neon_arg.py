def neon(num):
    sq = num*num # squares of number
    res = int()
    while sq > 0:
        last_digit = sq % 10
        res += last_digit
        sq //= 10
    if res == num:
        print(f'{num} is a Neon Number')
    else:
        print(f'{num} is not a Neon Number')
num = int(input('Enter a number:'))
neon(num)