num = int(input('Enter the number:'))
temp = num
res = int()
while(temp > 0):
    last_digit = temp%10
    res += last_digit
    temp = temp//10

print(f'sum of all digits of {num} is {res}')
