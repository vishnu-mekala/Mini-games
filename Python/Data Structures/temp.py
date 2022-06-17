#wap to perform linear search of list using enumerate
list = ['1','4','5','6','7','9','2','3','8']
search = input('Enter the key:')
for index, element in enumerate(list, start = 0):
    if element == search:
        print(f'{search} is present in the list {list} at index {index}')
        break
else:
    print(f'{search} is not present in the list {list}')

#wap to sort the given list
l = [18,11,199,98,2,4,13,11]
index = 0
while index < len(l):
    index2 = index + 1
    while index2 < len(l):
        if l[index] > l[index2]:
            temp = l[index]
            l[index] = l[index2]
            l[index2] = temp
        index2 += 1
    index += 1

print(l)


