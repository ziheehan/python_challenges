password1 = input("비밀번호를 입력하세요 : ")
password2 = input("한 번 더 입력해주세요 : ")
if password1 == password2 :
    print("Thank you")
elif password1.lower() == password2.lower():
    print("They must be in the same case")
else :
    print("Incorrect")
