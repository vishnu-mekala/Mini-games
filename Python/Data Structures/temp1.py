#wap to sort the given list in descending order
l = [18,11,199,98,2,4,13,11]
index = 0
while index < len(l):
    index2 = index + 1
    while index2 < len(l):
        if l[index] < l[index2]:
            temp = l[index]
            l[index] = l[index2]
            l[index2] = temp
        index2 += 1
    index += 1

#print(l)

#
list = ['a','d','e','i','u']
index = len(list) - 1
while index > -1:
    #print(list[index], end=' ')
    index -= 1


#
list = [1,8,8,8,3,4,2,3,8,7,8]
key = 8

count = 0
if key in list:
    print(f'{key} found')
    for index, letter in enumerate(list, start=1):
        if letter == key:
            print(f'It is at {index} location')
            count += 1
else:
    print('key not found')

if count > 0:
    print(count)