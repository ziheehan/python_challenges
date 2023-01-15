song = input("자장가의 첫 줄을 입력하세요 : ")
start = int(input("시작 인덱스 번호를 입력하세요 : "))
end = int(input("끝 인덱스 번호를 입력하세요 : "))
part = song[start : end]
print(part)
