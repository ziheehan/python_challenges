firstname = input("이름을 입력하세요 : ")
if len(firstname) < 5 :
    surname = input("성을 입력하세요 : ")
    name = firstname + surname
    name = name.upper()
    print(name)
else :
    firstname = firstname.lower()
    print(firstname)
