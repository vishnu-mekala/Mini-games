num = int(input('Enter the number:'))
temp = num

while(temp > 0):
    unit = temp%10
    print(unit)
    temp = temp//10