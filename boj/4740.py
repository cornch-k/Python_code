while True:
    a = input()
    if a == "***":
        break
    else:
        a = a[::-1]
        print(a)