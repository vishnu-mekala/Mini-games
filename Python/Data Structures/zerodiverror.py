print ('code started')

num1 = int(input('Enter a number:'))            #0
num2 = int(input('Enter another number:'))      #0

try:
    print(f'{num1/num2}')
except ZeroDivisionError:
    print("Don't divide by zero")
print ('code ended')