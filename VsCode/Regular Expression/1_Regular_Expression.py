import re

pattern = re.compile("Search in this text")
String = 'Search in this text!!!'

a = pattern.search(String)
b = pattern.findall(String)
c = pattern.fullmatch(String)
d = pattern.match(String)

mylist = []
mylist.append(a)
mylist.append(b)
mylist.append(c)
mylist.append(d)
print(mylist)