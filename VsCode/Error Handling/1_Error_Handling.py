# Error Handling 

while True:
    try:
        age = int(input("What is your age : "))
        10/age
    except ValueError as err:
        print(f"Please Enter a Number, Error : {err} ")
    except ZeroDivisionError as err:
        print(f"Please Enter age higher than zero \'0\' , Error : {err} ")
    else:
        print(f"Nice, Your age is {age}")
        break
    finally: 
        print("OK, this program is Done")



# To throw a Error Explicitly : 

# try:
#     raise ValueError("Its and Error")
# except:
#     print("Its and Error")
 