nums = [ 297,192,394,869]
for i in nums :
    print(i)
choice = int(input("리스트에서 숫자를 고르세요 : "))
if choice in nums :
    print(choice,"는", nums.index(choice),"번 째이다.")
else :
    print("That is not in the list")
