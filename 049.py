compnum = 50
cnt = 0
while True :
    num = int(input("숫자를 입력하세요 :"))
    cnt += 1
    if num < 50:
        print("up!")
    elif num > 50 :
        print("down!")
    elif num == 50 :
        print("Well done, you took",cnt,"attempts")
        break
        
