def main():
    num = int(input('Enter the value:'))
    status = is_armstrong(num)
    display(num)

def display(num):
    if main is True:
        print(' It is an amrstrong number')
    else:
        print('It is not an amrstrong number')

def is_armstrong(num):
    if armstrong_op(num) == num:
        return True
    return False

def armstrong_op(num):
    count = len(str(num))    #count of digits
    res = 0
    while num:
        last_digit = num % 10 #get last digit 
        res += last_digit ** count
        num //= 10 #remove last digit
    return res

main()





















# filter()
# map()
# reduce()
# lambda expression (sorting,etc)