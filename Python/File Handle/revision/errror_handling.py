print ('code started')

try: #plan A
    num1 = int(input('Enter a number:'))          
    num2 = int(input('Enter another number:'))   
    print(f'{num1/num2}')

except Exception as error: #Plan B
    print('Something is wrong', error)

finally:
    print('this will run no matter what')

raise ZeroDivisionError() #explicitly cause an error
print ('code ended')            
#Python is an interpreted language, will execute one line/code at a time. so it doesn't reach line 14