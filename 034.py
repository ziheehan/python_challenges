print("1) Square ")
print("2) Triangle\n")
choice = int(input("Enter a number:"))
if choice == 1 :
    legth = int(input("정사각형의 한 변의 길이를 입력하세요 : "))
    print("정사각형의 넓이는",legth**2,"입니다")
elif choice == 2 :
    base = int(input("삼각형의 밑변의 길이를 입력하세요 :"))
    height = int(input("삼각형의 높이를 입력하세요 :"))
    print("삼각형의 넓이는",base * height *0.5, "입니다")
else :
    print("숫자를 잘 못 입력했습니다.")

