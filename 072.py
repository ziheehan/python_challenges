subject = ["수학","과학", "영어", "체육","도덕","사회"]
print(subject)
choice = input("위 과목 중 좋아하지 않는 과목을 입력하세요 : ")
index = subject.index(choice)
del subject[index]
print(subject)
