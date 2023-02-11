from array import *
import random
nums1 = array('i', [])
nums2 = array('i', [])

for i in range(0, 3) :
    num = int(input("숫자를 입력하세요:"))
    nums1.append(num)
for i in range(0,5) :
    num = random.randint(1, 100)
    nums2.append(num)
nums1.extend(nums2)
nums1 = sorted(nums1)
for i in nums1 :
    print(i)
