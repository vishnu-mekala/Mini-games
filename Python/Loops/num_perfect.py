start = 1
count_perfect_number = int(input('Enter a number:'))
found_perfect_number = 0
num = 2
while found_perfect_number < count_perfect_number:
    count_of_factors = 0
    for div in range(start,num):
        if num % div == 0:
            count_of_factors += 1
    if count_of_factors == found_perfect_number:
        print(f'{num} is a PERFECT NUMBER')
        found_perfect_number += 1
    num+=1