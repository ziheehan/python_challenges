from array import *
nums = array('i', [1, 1, 2, 3, 4])
for i in nums :
    print(i)
num = int(input("배열 속 숫자들 중 하나를 입력하세요 :"))
if nums.count(num) == 1 :
    print(num,"은 배열에 1개 있습니다.")
else :
    print(num, "은 배열에", nums.count(num),"개 있습니다.")
