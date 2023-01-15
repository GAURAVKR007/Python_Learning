import datetime
import time
from array import array

print(datetime.time(5,45,2))
print(datetime.date.today())
print(time.time())

arr = array('i',[1,2,3,4,5])
for i in range(len(arr)):
    print(arr[i],end=" ")