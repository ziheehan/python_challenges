name = input("이름을 입력하세요 : ")
num = int(input("숫자를 입력하세요 : "))
if num < 10 :
    for i in range(0,num):
        print(name)
else:
    print("Too high")
