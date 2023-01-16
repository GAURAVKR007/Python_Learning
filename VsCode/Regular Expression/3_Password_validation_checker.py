import re

pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
# The regular expression Above cheks that a password:

# Has minimum 8 characters in length. Adjust it by modifying {8,}
# At least one uppercase English letter. You can remove this condition by removing (?=.*?[A-Z])
# At least one lowercase English letter.  You can remove this condition by removing (?=.*?[a-z])
# At least one digit. You can remove this condition by removing (?=.*?[0-9])
# At least one special character,  You can remove this condition by removing (?=.*?[#?!@$%^&*-])

while True: 
    password = input("Enter the Password : ")

    if len(password) > 8:
        if(pattern.fullmatch(password)):
            print("Password is Valid")
            break
        else:
            print("Password is Invalid, Try Again!")
            continue
    else:
        print("Password should Contain At least 8 Letters, Try Again!")
        continue