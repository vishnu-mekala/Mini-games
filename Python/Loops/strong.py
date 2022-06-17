num = int(input('Enter a number:'))
temp = num
sum = 0

while temp:
    n =  1
    fact = 1
    last_digit = temp % 10
    while n <= last_digit: 
        fact *= n 
        n += 1
    sum += fact
    temp = temp//10

if (sum == num):
    print(f'{num} is a strong number')
else:
    print(f'{num} is not a strong number')