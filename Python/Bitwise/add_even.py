#even numbers from 1-20 in a list
from xml.dom import minidom


list = list()
for var in range(1,20+1):
    if var % 2 == 0:
        list.append(var)
print(list)

#add all the elements in the list:
list = list()
sum = 0
for var in range(1,20+1):
        sum += var
        list.append(var)
print(f'{list} and its {sum=}')

#to find greatest value of the list
list = list()
for var in range(1,20+1):
        list.append(var)
print(f'{list} and its maximum value is {var}')

