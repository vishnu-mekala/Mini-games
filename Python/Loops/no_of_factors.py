start = 1
stop = int(input('Enter a number:'))
step = 1
count = 0
for var in range(start,stop+1):
    if stop % var == 0:
        count += step
print (f'{count}')
