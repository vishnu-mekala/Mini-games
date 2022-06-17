# wap to generate dictionary of first n natural numbers where key is the natural number and value is the square of the number-
# nat=dict()
# n = int(input('Enter the Maximum Range Value:'))
# for i in range(1,n+1): #n = end range value
#     nat[i]=i**2
# print(nat) 

# wap to add a given key value to a dictionary - 
# u = dict()
# n = 5
# for i in range(1,n+1):
#     u[i]=i**2
# u[6] = 36
# print(u)

# wap to merge given dictionary - 
# d1 = {1:10,2:20}
# d2 = {3:30,4:40}
# d3 = {5:50,6:60}
# d ={}
# for key in d1:
#     d[key] = d1[key]
# for key in d2:
#     d[key] = d2[key]
# for key in d3:
#     d[key] = d3[key]
# print(d)
#     #and
# d1.update(d2)
# d1.update(d3)
# print(d1)

# wap to sort a given dictionary based on keys - 
# d = {3:'c',5:'e',2:'b',1:'a',7:'g',4:'d',6:'f'}
# for key in sorted(d):
#     print(f'{key}:{d[key]}', end=' ')

# wap to sort a given dictionary based on values - 
d = {3:'g',5:'b',2:'a',1:'f',7:'e',4:'d',6:'c'}
d1 = d.reverse
for value in sorted(d):
    print(f'{d[value]}:{value}', end=' ')
