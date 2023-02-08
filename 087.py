word = input("단어를 입력하세요 :")
length = len(word)
num = 1
for i in word :
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1
