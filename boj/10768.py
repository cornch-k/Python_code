Month = int(input())
Day = int(input())
if Month == 2 and Day == 18:
    print("Special")
elif Month >= 3 or Month >= 2 and Day >18:
    print("After")
elif Month <= 1 or Month <= 2 and Day < 18:
    print("Before")