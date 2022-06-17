#wap to delete all th duplicates from a given list
l = [1,2,2,3,3,4,4,5,6,7,7,7]
remove = []
for i in l:
    if i not in remove:
        remove.append(i)
print(remove)

#wap to sort the list in descending order
l = [1,2,3,8,9,7,6,4,5]
sorted_list = sorted(l)[::-1]
print(sorted_list)

#wap to generate list of prime numbers
l = []
for i in range(1,10):
    