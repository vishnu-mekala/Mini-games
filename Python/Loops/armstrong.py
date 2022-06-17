num = int(input('Enter a number:'))
count_of_digits = 0

temp = num
while temp:
    temp //= 10
    count_of_digits += 1

temp = num
res = 0
while temp:
    last_digit = temp % 10
    res = res + (last_digit ** count_of_digits)
    temp //= 10

if num == res:
    print(f'{num} is Armsrong')
else:
    print(f'{num} is not an Armsrong')
