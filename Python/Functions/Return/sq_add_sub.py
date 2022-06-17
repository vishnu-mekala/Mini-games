def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def square(num):
    return num ** 2

num1 = int(input('Enter a number:'))
num2 = int(input('Enter a number:'))
sum_res = add(num1, num2)
diff_res = sub(num1, num2)
#sq_res = square(sum_res)
#sq_diff = square(diff_res)
#res = add(sq_res,sq_diff)

#print(f'Sum of squares = {res}')
print(f'Difference of squares = {sub(square(sum_res), square(diff_res))}')
print(f'Sum of squares = {add(square(sum_res), square(diff_res))}')