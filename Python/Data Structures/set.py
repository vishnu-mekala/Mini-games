# Set = It is an unordered collection of unique objects

# # 1) wap to create a set of first 10 prime numbers.
# s = set()
# num_prime = 10   #count prime
# found_prime = 0   #found prime
# num = 2
# while found_prime != num_prime:
#     count = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             count +=1
#     if count == 2:
#         s.add(num)
#         found_prime += 1
#     num+=1
# print(s)


# 2) wap to create a set of first 10 amstrong numbers.
# a = set()
# num_amstrong = 10
# found_armstrong = 0
# num = 1
# count_of_digits = 0
# temp = num
# while temp:
#     temp //= 10
#     count_of_digits += 1
# temp = num
# res = 0
# while found_armstrong != num_amstrong:
#     for i in range(1, num+1):
#         while temp:
#             last_digit = temp % 10
#             res = res + (last_digit ** count_of_digits)
#             temp //= 10
#     if num == res:
#         a.add(num)
#         found_armstrong += 1
#     num +=1 
# print(a)

def start():
    set_armstrong = armstrong()
    display(set_armstrong)

def armstrong():
    num = 1
    to_find = 20
    a = set()
    while to_find:
        if armstrong_op(num) == num:
            a.add(num)
            to_find -= 1
        num += 1
    return a

def armstrong_op(num):
    count = len(str(num))
    res = 0
    while num:
        last_digit = num % 10
        res += pow(last_digit, count)
        num //= 10
    return res

def display(set_armstrong):
    print(set_armstrong)

start()