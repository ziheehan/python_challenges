from array import *
nums = array('i', [])
for i in range(0, 5) :
    num = int(input("숫자를 입력하세요:"))
    nums.append(num)
nums = sorted(nums)
for i in nums :
    print(i)
num = int(input("배열에서 숫자를 골라 입력하세요 :"))
if num in nums :
    nums.remove(num)
    num2 = array('i',[])
    num2.append(num)
    print(nums)
    print(num2)
else :
    print("배열의 값이 아닙니다.")
