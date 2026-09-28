N = int(input())
NBinary = ""
while N > 0:
    if (N % 2) == 0:  # 숫자가 짝수면 0
        NBinary += "0"
    elif (N % 2) == 1:
        NBinary += "1"
    N //= 2
print(NBinary[::-1].zfill(10))
