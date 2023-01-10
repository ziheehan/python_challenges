rain = input("지금 비가 오나요?")
rain = rain.lower()
if rain == "yes" :
    wind = input("바람이 부나요?")
    wind = wind.lower()
    if wind == "yes" :
        print("It is too windy for an umbrella")
    else :
        print("Take an umbrella")
else :
    print("Enjoy your day")
