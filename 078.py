drama = ["You", "The end of the fucking world","La casa de papel", "The Glory"]
for i in drama:
    print(i)
newdrama = input("다른 드라마를 입력하세요 : ")
position = int(input("0과 3 사이의 숫자를 입력하세요 :"))
drama.insert(position, newdrama)
for i in drama :
    print(i)
