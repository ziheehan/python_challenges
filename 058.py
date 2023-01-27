import random
score = 0
for i in range(1, 6) :
   num1 = random.randint(1,50)
   num2 = random.randint(1,50)
   correct = num1 + num2
   print(num1, "+", num2, "=")
   answer = int(input("answer : "))
   if answer == correct :
        score = score + 1
print("Your scored", score, "out of 5")
