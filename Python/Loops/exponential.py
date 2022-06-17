num = int(input('Enter the base number:'))
num1 = int(input('Enter the power number:'))
n = 1
exp = 1

while n <= num1:
    exp = exp*num
    n += 1

print(f'{num} to the power {num1} is {exp}')