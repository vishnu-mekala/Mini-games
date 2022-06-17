start = 1
stop = 20
step = 1
found = 0
count = 0

for div in range(start,stop+1):
    if stop % div == 0:
        count += 1
if count == 2:
    print(stop)
    found +=1
stop+=1