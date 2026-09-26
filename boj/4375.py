while True :
    try :
        n = int(input())
    except :
        break

    number = 0
    count = 1
    while True:
        number = number * 10 + 1
        number %= n
        if number == 0:
            print(count)
            break
        else:
            count += 1