handle = open('C:\\HEYA6\\Python\\File Handle\\demo.txt')   #copy_path

remove = ()
for line in handle:
    print(line, end='')
    for i in line:
        if i not in remove:
            remove.append(line)
print(remove)



wap to count duplicate words in each sentence
wap to count duplicate letters in each sentence and mention