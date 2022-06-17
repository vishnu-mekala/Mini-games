s = input('Enter a string:')
key = input('Enter the key to search:')

count = 0
if key in s:
    print(f'{key} found')
    for index, letter in enumerate(s, start=1):
        if letter == key:
            print(f'It is at {index} location')
            count += 1
else:
    print('key not found')

if count > 0:
    print(count)