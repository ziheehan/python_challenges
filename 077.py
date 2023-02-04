party = []
party.append(input("파티에 초대할 이름을 입력하세요 : "))
party.append(input("파티에 초대할 이름을 입력하세요 : "))
party.append(input("파티에 초대할 이름을 입력하세요 : "))
answer = input("다른 사람을 추가하겠습니까?")
while answer == "y" :
    name = party.append(input("초대할 사람의 이름을 입력하세요:"))
    answer = input("다른 사람을 추가하겠습니까?")
print("파티에", len(party),"명 초대했습니다.")
print(party)
choice = input("위 이름 중 하나를 입력하세요 : ")
print(choice,"는", party.index(choice),"번 째에 있습니다.")
come = input("이 사람을 초대하고 싶습니까?(y/n)")
if come == "n" :
    party.remove(choice)
print(party)
