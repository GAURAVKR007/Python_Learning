# with open('test1.txt',mode='r') as my_file:                            # Read 
#     print(my_file.readlines())
    
# with open('test2.txt',mode='w') as my_file2:
#     text = my_file2.write('This is the Seocnd file test2.txt')       # Write 
#     print(text)

with open('test2.txt',mode='a') as my_file3:                          # Append
    text2 = my_file3.write('\nI am Appending in test2.txt')
    print(text2) 