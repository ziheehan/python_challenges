message = input("대문자로 메시지를 입력하세요 : ")
tryagain = True
while tryagain == True:
    if message.isupper():
        print("Thank you")
        tryagain = False
    else :
        print("Try again")
        message = input("대문자로 메시지를 입력하세요 : ")
