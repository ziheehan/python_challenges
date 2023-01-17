import math
radius = int(input("원기둥 밑면의 반지름을 입력하세요 : "))
height = int(input("원기둥의 높이를 입력하세요 :"))
area = math.pi * (radius**2)
volume = area * height
print(round(volume, 3))
