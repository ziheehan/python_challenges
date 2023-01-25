import random
num = random.randint(1,5)
guess = int(input("1에서 5사이의 숫자를 입력하세요 :"))
if num == guess :
    print("Well done")
else :
    if num > guess :
        print("up")
    else :
        print("down")
    guess = int(input("다시 입력하세요 :"))
    if num == guess:
        print("Correct")
    else :
        print("You lose")
