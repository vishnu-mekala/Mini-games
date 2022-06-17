start = 1
count_prime = int(input('Enter a number:'))
found_prime = 0
num = 1
while found_prime != count_prime:
    count = 0
    for div in range(start,num+1):
        if num % div == 0:
            count +=1
    if count == 2:
        print(f'{num} is a PRIME NUMBER')
        found_prime += 1
    num+=1