party = []
party.append(input("파티에 초대할 이름을 입력하세요 : "))
party.append(input("파티에 초대할 이름을 입력하세요 : "))
party.append(input("파티에 초대할 이름을 입력하세요 : "))
answer = input("다른 사람을 추가하겠습니까?")
while answer == "y" :
    name = party.append(input("초대할 사람의 이름을 입력하세요:"))
    answer = input("다른 사람을 추가하겠습니까?")
print("파티에", len(party),"명 초대했습니다.")
