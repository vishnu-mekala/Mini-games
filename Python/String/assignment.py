#
s1 = input('Enter the string1:')
a1 = ord('A')
b1 = ord('Z')
c1 = ord(' ')

stat1 = False

for u in s1:
    if ord(u) in range(a1,b1) and c1:
        stat1 = True

if stat1 is True:
    print(f'The String is in Uppercase')
else:
    print(f'The String is not in Uppercase')

#
s2 = input('Enter the string2:')
a2 = ord('a')
b2 = ord('z')
c2 = ord(' ')

stat1 = False

for i in s2:
    if ord(i) in range(a2,b2) and c2:
        stat1 = True

if stat1 is True:
    print(f'The String is in Lowercase')
else:
    print(f'The String is not in Lowercase')



#
s = "     My   Name   is  Vishnu   "
x = s.split()
print(len(x))



#
