nums = []
count = 0
while count < 3 :
    num = int(input("숫자를 입력하세요 : "))
    nums.append(num)
    print(nums)
    count = count + 1
answer = input("마지막 숫자를 저장하시겠습니까?(y/n)")
if answer == "n":
    nums.remove(num)
print(nums)
