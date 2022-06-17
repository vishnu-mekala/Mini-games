def automorph(num):
    temp = num # value of num in temp
    sq = num*num # squares of number
    flag = True # assume the given num is an Automorphic Number

    while temp: # temp != o
        if temp % 10 != sq % 10: # finding last_digit of temp != last_digit of sq by dividing by 10 (%)
            flag = False 
        temp //= 10 # finding second last_digit of temp by // temp by 10
        sq //= 10 # finding second last_digit of sq by // sq by 10
    if flag is True:
        print(f'{num} is an Automorphic Number')
    else:
        print(f'{num} is not an Automorphic Number')

num = int(input('Enter a number:'))
automorph(num)