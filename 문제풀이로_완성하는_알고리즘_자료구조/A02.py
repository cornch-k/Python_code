# N개의 정수 A1, A2, ..., AN 안에 정수 X가 포함되어 있는지 판별하는 프로그램을 작성하십시오.

N, X = map(int, input().split())
numberList = list(map(int, input().split()))

if X in numberList:
    print("Yes")
else:
    print("No")
