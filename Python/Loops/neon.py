num = int(input('Enter a number:'))
sq = num*num # squares of number
temp = sq # value of num in temp
res = int()

while temp:
    last_digit = temp % 10
    res += last_digit
    temp //= 10

if res == num:
    print(f'{num} is a Neon Number')
else:
    print(f'{num} is not a Neon Number')