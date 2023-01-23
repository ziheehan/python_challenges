while True :
    num = int(input("10과 20 사이의 숫자를 입력하세요 :"))
    if num <= 10 :
        print("Too Low")
        continue
    elif num >=20 :
        print("Too high")
        continue
    else :
        print("Thank you")
        break
