from collections import Counter,defaultdict,OrderedDict

li = [1,2,3,4,4,5,6,7,7]
sentence = "Blah Blah Blah Blah"
print(Counter(li))                       # Count the Number of times something Appeared in list/Iterable
print(Counter(sentence))

simple_dict = defaultdict(lambda : 'Invalid\\Does not Exist',{'a' : 1,'b' : 2})      # Gives a default value for any key which is not Present
print(simple_dict['c'])

d1 = OrderedDict()               # Make a Dictionary Ordered
d1['a'] = 10
d1['b'] = 20

d2 = OrderedDict()
d2['b'] = 20
d2['a'] = 10

print(d1 == d2)