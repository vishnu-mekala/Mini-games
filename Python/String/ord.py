s = input('Enter your character:')
#if (ord(s) >= 65 and ord(s)<= 90):
    #print('The given character is an Uppercase')
#elif (ord(s)>=97 and ord(s)<=122):
    #print('The given character is a Lowercase')
#else:
    #print('The given character is neither Uppercase nor Lowercase')
a = ord('A')
b = ord('Z')
u = ord(s[0])
if u in range(a,b):
    print('First char is Uppercase')
else:
    print('First char is not Uppercase')