import random
num = random.randint(1,10)
while True :
    guess = int(input("1에서 10사이의 숫자를 입력하세요 :"))
    if num > guess :
        print("up")
    elif num < guess :
        print("down")
    elif num == guess :
        print("Correct")
        break
