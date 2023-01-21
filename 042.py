total = 0
for i in range (0,5) :
    num = int(input("숫자를 입력하세요 : "))
    answer = input("숫자를 total에 더하겠습니까?(y/n)")
    if answer == 'y' :
        total += num
print(total)
