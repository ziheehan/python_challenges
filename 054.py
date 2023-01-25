import random
coin = random.choice(['h','t'])
ht = input("앞면과 뒷면 중 하나를 입력하세요(h/t) :")
if ht == coin :
    print("You win")
else :
    print("Bad luck")
print(coin, "(이)었습니다.")
