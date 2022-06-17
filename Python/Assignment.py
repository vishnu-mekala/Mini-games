# #wap to convert the given digit into its string value.
# input = int(input('Enter the num between 0 to 9:'))
# numeric = [0,1,2,3,4,5,6,7,8,9]
# words = ["zero","one","two","three","four","five","six","seven","eight","nine"]

# for h in numeric:
#     if input == h:
#         print(words[h])

num = (input('Enter the num between 0 to 9:'))
dict = { "0" : "zero" , "1":"one " , "2" : "two" , "3" : "three" , "4" : "four" , "5" : "five" , "6" : "six" , "7" : "seven" , "8" : "eight" , "9" : "nine"}

for i in num :
      print( dict [ i ], end = " ")