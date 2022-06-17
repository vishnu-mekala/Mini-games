def perfect(start,stop):
    for var in range(start,stop+1):
        res = 0
        for i in range(1,var):
            if var % i == 0:
                res += i
        if var == res:
            print(f'{res} is a Perfect Number')
start = int(input('Enter the starting value:'))
stop = int(input('Enter the ending value of range:'))
perfect(start,stop)
