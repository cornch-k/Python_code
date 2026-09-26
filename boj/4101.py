while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    elif A > B:
        print("Yes")
    else:
        print("No")