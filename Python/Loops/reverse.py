num = int(input('Enter the number:'))
temp = num
res = int()
while temp:
    last_digit = temp % 10
    res = res * 10 + last_digit
    temp //=10

print(f'{num} reverse is {res}')

