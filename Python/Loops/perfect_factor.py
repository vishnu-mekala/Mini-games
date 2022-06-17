start = 1
stop = int(input('Enter a number:'))
step = 1
res = 0

for var in range(start,stop):
    if stop % var == 0:
        res += var
if res == stop:
    print(f'{stop} is a perfect number')
else:
    print(f'{stop} is a not a perfect number')