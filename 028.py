word = input("단어를 입력하세요 : ")
first = word[0].lower()
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u" :
    newword = rest + first + "ay"
else :
    newword = word + "way"
print(newword.lower())

