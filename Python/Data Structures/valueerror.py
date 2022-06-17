print ('code started')

try:
    num1 = int(input('Enter a number:'))          #A  
    num2 = int(input('Enter another number:'))   
    print(f'{num1/num2}')

except Exception as error:
    print('Something is wrong', error)

finally:
    print('this will run no matter what')

raise ZeroDivisionError()

print ('code ended')