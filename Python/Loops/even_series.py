num = int(input('Enter a number:'))
count = 0
n = 1
while count < num:
    if n % 2 == 0:
        print(n)
        count+=1
    n+= 1