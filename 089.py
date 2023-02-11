from array import *
import random
nums = array('i',[])
for i in range(0,5):
    num = random.randint(1, 100)
    nums.append(num)
for i in nums :
    print(i)
