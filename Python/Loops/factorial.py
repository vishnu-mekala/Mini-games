num = int(input('Enter a number:'))
n =  1
fact = 1

while n <= num:
    fact *= n 
    n += 1

print(f'{num}! is {fact}')
