# #
# list = [1,2,34,45,6,7,8,46]
# max = list[0]
# for var in list:
#     if var > max:
#         max = var
# print(max)

# #find the 2nd greatest value in a list.
# list = [17,40,25,18,8,22,11]
# maxi = list[0]
# second_maxi = 0
# for var in list:
#     if var > maxi:
#         second_maxi = maxi
#         maxi = var
#     elif var > second_maxi and var < maxi:
#         second_maxi = var
# print(f'Second Greatest: {second_maxi}')

# #find the lowest value in a list.
# list = [17,40,25,18,8,22,11]
# min = 0
# for var in list:
#     if var < min:
#         min = var

# print(f'Lowest: {min}')

# #find the 2nd lowest value in a list.
# list = [17,40,25,18,8,22,11]
# lowest = list[0]
# second_lowest = list[0]
# for var in list:
#     if var < lowest:
#         second_lowest = lowest
#         lowest = var
#     elif var < second_lowest and var > lowest:
#         second_lowest = var

# print(f'Second Lowest: {second_lowest}')

#wap to insert an element for a given location/position:
from enum import unique


list = [2,3,5,7,11,13]
element = 17
position = 7
l = list[ :position-1] + [element]
l = l + list[position-1: ]
print(l)

#wap to remove the duplicate values of an element in the given list:
l = [2,1,2,4,3,5,2,2,3,2,1,7]
index = 0
for var in l:
    while l.count(var) > 1:
        l.pop(l.index(var, l.index(var) + 1))
# remove = [i for n, i in enumerate(list) if i not in list[:n]]
# remove = []
# for i in list:
#     if i not in remove:
#         remove.append(i)
# print(remove)
print(l)