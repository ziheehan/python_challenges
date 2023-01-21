count = input("카운트 업/다운(u/d)?")
if count == 'u' :
    num = int(input("가장 큰 숫자를 입력하세요 :"))
    for i in range(1, num+1):
        print(i)
elif count == 'd' :
    num = int(input("20미만의 숫자를 입력하세요 :"))
    for i in range(20, num-1,-1):
        print(i)
else :
    print("I don''t understand")
