my_file = open('test1.txt')

print(my_file.read())
my_file.seek(0)              # Because the Python use cursor to read the file 
print(my_file.read())
my_file.seek(0)

print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())

my_file.close()