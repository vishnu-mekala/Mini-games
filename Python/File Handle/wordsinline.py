# wap to read sentences from a file and display the number of words in each sentence

handle = open('C:\\HEYA6\\Python\\File Handle\\demo.txt')   #copy_path

data = handle.readline().split()
while data:
    print(len(data))
    data = handle.readline().split()

# x = b.split()
# y = c.split()
# z = d.split()

# print(len(a))
# print(len(x))
# print(len(y))
# print(len(z))
