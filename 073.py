food_dictionary = {}
food1 = input("좋아하는 음식을 입력하세요 : ")
food_dictionary[1] = food1
food2 = input("다른 좋아하는 음식을 입력하세요 : ")
food_dictionary[2] = food2
food3 = input("다른 좋아하는 음식을 입력하세요 : ")
food_dictionary[3] = food3
food4 = input("다른 좋아하는 음식을 입력하세요 : ")
food_dictionary[4] = food4
print(food_dictionary)
delete = int(input("지우고 싶은 음식의 번호를 입력하세요 : "))
del food_dictionary[delete]
print(sorted(food_dictionary.values()))
