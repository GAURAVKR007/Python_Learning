try:
    with open('Text_Content/test3.txt',mode='r') as my_file:      # Realtive Path of the File 
        print(my_file.readlines())
except FileNotFoundError as err:
    print("File does not Exist")
    raise err
except IOError as err:
    print("IO Error")
    raise err