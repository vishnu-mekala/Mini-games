s = input('Enter a string:')
key = input('Enter the key to search:')

if key in s:
    print(f'{key} found')
    for index, letter in enumerate(s, start=1):
        if letter == key:
            print(f'It is at {index} location')
else:
    print('key not found')