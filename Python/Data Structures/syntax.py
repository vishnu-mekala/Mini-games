#list
#DLL
l = [1,2,34,45,6,7,8,'Nine','X']
print(type(l))
print(l)
l = list()
print(type(l))


for var in range(1,20+1):
    if var % 2 == 0:
        print(var)
    l.append(var)
print(l)