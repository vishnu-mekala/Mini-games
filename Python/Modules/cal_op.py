import cal
def main():
    while True:         #using 'while True:' we can run this code forever
        choice = menu()
        op(choice)

def menu():
    print('1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit')
    return read('Make a Choice 1,2,3,4 or 5:')

def op(choice):
    if choice == 5:
        exit()
    num1 = read('Enter 1st Num:')
    num2 = read('Enter 2nd Num:')
    if choice == 1:
        print(f'sum of {num1} & {num2} is {cal.add(num1, num2)}')
    elif choice == 2:
        print(f'difference of {num1} & {num2} is {cal.sub(num1, num2)}')
    elif choice == 3:
        print(f'product of {num1} & {num2} is {cal.mul(num1, num2)}')
    elif choice == 4:
        print(f'division of {num1} & {num2} is {cal.div(num1, num2)}')
    else:
        print('Invalid choice.\nChoose again')

def read(msg):
    return int(input(msg))

main()