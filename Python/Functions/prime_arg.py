def prime(stop):
    start = 1
    step = 1
    count = 0
    for var in range(start,stop+1):
        if stop % var == 0:
            count += 1
    if count == 2:
        print(f'{stop} is a prime number')
    else:
        print(f'{stop} is a not a prime number')
stop = int(input('Enter a number:'))
prime(stop)