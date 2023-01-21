party = int(input("파티에 몇 명을 초대할까요?"))
if party < 10 :
    for i in range(0, party) :
        name = input("이름이 뭔가요?")
        print(name,"has been invited")
elif party >= 10 :
    print("Too many people")
    
