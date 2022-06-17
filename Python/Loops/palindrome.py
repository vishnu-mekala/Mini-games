num = int(input('Enter the number:'))
temp = num
res = int()
while temp:
    last_digit = temp % 10
    res = res * 10 + last_digit
    temp//=10
if res == num:
    print((f'{res} is a palindrome number'))
else:
    print((f'{res} is not a palindrome number'))