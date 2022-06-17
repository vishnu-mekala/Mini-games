# Pattern Matching a (using case = numeric)
# code = int(input('Enter the code: '))
# match code:
#     case 100:
#         print('Code Green')
#     case 104:
#         print('Code Red')
#     case 404:
#         print('Code Errpr')
#     case _:
#         print('Code Not Found')

# b (using case = variables)
# code = int(input('Enter the code: '))
# HEYA6 = 100
# match code:
#     case HEYA6 :    #variable act as a wildcard same like "_"
#         print('Code Green')
#     case 104:
#         print('Code Red')
#     case 404:
#         print('Code Errpr')
#     case _:
#         print('Code Not Found')

# c (using class)
# code = int(input('Enter the code: '))
# class abc:
#     CODE_GREEN = 100
#     CODE_ERROR = 404
# match code:
#     case abc.CODE_GREEN:
#         print('Code Green')
#     case 104:
#         print('Code Red')
#     case abc.CODE_ERROR:
#         print('Code Errpr')

# d (using list)
l = {'food':'pasta','milkshake':'mango'}
match l:
    case {'milk':x}:
        print(f'first milk n then {x}')
    case {'food'x}:
        print(f'first food n then {x}')