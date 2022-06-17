handle = open('C:\\HEYA6\\Python\\File Handle\\demo.txt')   #copy_path

# for line in handle:
#     print(line,end='')

# print(handle.read())

data = handle.readline()
while data:
    print(data,end='')
    data = handle.readline()
