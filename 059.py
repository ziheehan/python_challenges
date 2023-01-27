import random
color = random.choice(["검", "흰", "파", "초", "노"])

while True :
    answer = input("검, 흰, 파, 초, 노 중 하나를 고르세요 :")
    if color == answer:
        print("Well done")
        break
    else :
        print("다시 입력하세요!")
