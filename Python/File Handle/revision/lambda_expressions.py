# solve an expression 4x^3 + 3x^2 + 2x + 4
# from math import sqrt
# Root = lambda a,b,c: ((-b + sqrt((b*b) - (4 * a * c))) / (2 * a), (-b + sqrt((b*b) - (4 * a * c))) / (2 * a))
# print(Root(4,3,2))


# f = lambda a : 4*a**3 + 3*a**2 + 2*a + 4
# f = lambda a : a**4 + a**3 + a**2 + 4*a + 10
# print(f(4))
# print(f(5))

#merge last name & first name
# first_name = (input('Enter the first name:'))
# last_name = (input('Enter the last name:'))

# full_name = lambda first_name, last_name : first_name.strip().title() + ' ' + last_name.strip().title()
# print(full_name(first_name,last_name))

#arithmetic mean
# num1 = int(input('Enter num1:'))
# num2 = int(input('Enter num2:'))
# a_mean =  lambda *args : sum(args)/len(args)
# print(a_mean(num1,num2))

#geometric mean
# num1 = int(input('Enter num1:'))
# num2 = int(input('Enter num2:'))
# g_mean =  lambda num1,num2 : (num1*num2)**0.5
# print(g_mean(num1,num2))

#harmonicc mean
num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))
num3 = int(input('Enter num3:'))
h_mean =  lambda num1,num2,num3 : 3/(1/num1 + 1/num2 + 1/num3)
print(h_mean(num1,num2,num3))



