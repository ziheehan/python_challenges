from array import *
nums = array('i', [])
while len(nums) < 5 :
    num == int(input("10에서 20사이의 숫자를 입력하세요 :"))
    if num >= 10 and num <= 20 :
        nums.append(num)
    else:
        print("범위를 벗어났습니다")
for i in nums:
    print(i)
