cnt = 0
while True :
    name = input("초대할 사람의 이름을 입력하세요 :")
    print(name, "has now been invited")
    cnt += 1
    answer = input("더 초대하겠습니까?(y/n)")
    if answer == 'y':
        continue
    else :
        print(cnt,"명이 초대되었습니다..")
        break
