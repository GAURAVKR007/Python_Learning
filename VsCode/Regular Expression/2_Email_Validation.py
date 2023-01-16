import re

pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')        # Regular Expression for Email

email = "gauravkrthakur007@gmail.com"
a = pattern.search(email)
print(a)

if pattern.fullmatch(email):
    print("Email Valid")
else:
    print("Email Invalid")