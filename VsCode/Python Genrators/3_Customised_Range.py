class MyRange():
    current = 0
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyRange.current <= self.last:
            num = MyRange.current
            MyRange.current += 1
            return num
        raise StopIteration

special_range = MyRange(0,100) 
for i in special_range:
    print(i)
