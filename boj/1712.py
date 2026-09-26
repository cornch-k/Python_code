
a, b, c = map(int, input("입력하세요 >>").split())
if b >= c:
    print(-1)
else:
    print(int(a/(c - b)+1))