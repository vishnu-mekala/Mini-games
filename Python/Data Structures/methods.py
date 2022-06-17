# #wap to merge two lists
# l =[]
# for i in range (1,10):
#     l.append(i)
# ll = list(range(1,10))
# print(l+ll)

# l.extend(l) #This method is used to merge two lists into one
# print(l)

# print(l.count(11)) #This is used to count the occurances of given arguement

# #wap to generate a copy of given list
# print(l.copy()) #This is used to generate a copy of the calling list
# l1 = []
# for var in l:
#     l1.append(var)
# print(l1)
# print(id(l), 'is not same as', id(l1))

#wap to delete a given element from the list
# list = [1,2,3,4,7,8,8,8,5,6,11,23]
# element = 8                    
# l=[]
# for var in list:
#     if var != element:
#         l.append(var)
#     else:
#         continue
# print(list)
# print(l)


# list.remove(8)
# print(list) #It is an inbuilt method of list class used to remove a given element from the list 
# #Note: It removes only the first occurance
# #Note: If we try to remove the element which is not present in list, it gives error stating "ValueError: list.remove(x): x not in list"

#wap to remove an element from a given location
list = [2,3,5,5,2,1,3,9]
# position = 5
# l = list[:position-1]
# l = l + list[position:]
# print(l)

# print(list.pop(position-1)) #remove an element from a given location
# print(list)

print(list.index(9)) #to find the loc/index of the given value

#wap to insert an element at given position
list.insert(5,6)
print(list)