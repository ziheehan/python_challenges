num1 = int(input("숫자를 입력하세요 :"))
num2 = int(input("숫자를 입력하세요 : "))
answer = num1 + num2
while True :
    choice = input("숫자를 더 입력하고 싶은가요?(y/n)")
    if choice == 'y' :
        num3 = int(input("숫자를 입력하세요 :"))
        answer = answer + num3
        continue
    else :
        print(answer)
        break
