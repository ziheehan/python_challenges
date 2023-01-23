bottles = 5
while bottles > 0:
    print("There are",bottles,"green bottles hanging on the wall")
    print(bottles, "green bottles hanging on the wall")
    print("And if 1 green bottle should accidentally fall,")
    bottles -= 1
    answer = int(input("How many green bottles hanging on the wall?"))
    if answer == bottles:
        print("There will be", bottles,"green bottles hanging on the wall")
    else :
        while answer != bottles:
            answer = int(input("No try again : "))
print("There are no more green bottles hanging on the wall")
