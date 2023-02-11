name = input("이름을 입력하세요 :")
count = 0
name = name.lower()
for i in name :
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count = count + 1
print("모음은",count,"개 입니다.")
