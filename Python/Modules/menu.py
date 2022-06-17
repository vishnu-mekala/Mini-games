import common
from armstrong import is_armstrong
from prime import is_prime
def start():
    while True:
        choice = menu()
        op(choice)
def menu():
    print('1.Prime\n2.Armstrong\n3.Exit\n4.Update')
    return common.read('Enter your choice:')
def op(num):
    if common.is_equal(num, 3):
        exit()
    if common.is_equal(num, 4):
        import importlib as imp
        imp.reload(common)
    else:
        if common.is_equal(num, 1):
            print('You want to check if a given number is prime or not?')
            num = common.read('Enter the number:')
            is_prime(num)
        elif common.is_equal(num, 2):
            print('You want to check if a given number is armstrong or not?')
            num = common.read('Enter the number:')
            is_armstrong(num)

start()