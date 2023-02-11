from array import *
nums = array('i', [])
for i in range(0, 5):
    num = int(input("숫자를 입력하세요 :"))
    nums.append(num)
nums = sorted(nums)
nums.reverse()
print(nums)
